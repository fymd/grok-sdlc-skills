// tests/store.test.js — utils/store.js 逻辑单测（Node 运行，零依赖）
// 运行：node tests/store.test.js
const assert = require('assert');
const path = require('path');

// ---- mock 微信本地 Storage ----
const storage = {};
global.wx = {
  getStorageSync: (k) => storage[k],
  setStorageSync: (k, v) => { storage[k] = v; },
};

const STORE_PATH = path.join(__dirname, '..', 'utils', 'store.js');
const store = require(STORE_PATH);

let passed = 0, failed = 0;
function test(name, fn) {
  delete storage['todos'];
  try { fn(); passed++; console.log('ok   -', name); }
  catch (e) { failed++; console.error('FAIL -', name, '\n     ' + e.message); }
}

test('初始为空', () => {
  assert.deepStrictEqual(store.load(), []);
});

test('add 返回自增 id，默认未完成', () => {
  const a = store.add('写文档');
  assert.strictEqual(a.id, 1);
  assert.strictEqual(a.title, '写文档');
  assert.strictEqual(a.done, false);
  const b = store.add('买菜');
  assert.strictEqual(b.id, 2);
  assert.strictEqual(store.load().length, 2);
});

test('add 会 trim 标题', () => {
  const a = store.add('  前后空格  ');
  assert.strictEqual(a.title, '前后空格');
});

test('add 空/纯空白/undefined 返回 null 且不入库', () => {
  assert.strictEqual(store.add(''), null);
  assert.strictEqual(store.add('   '), null);
  assert.strictEqual(store.add(undefined), null);
  assert.strictEqual(store.load().length, 0);
});

test('持久化：冷启动后数据仍在', () => {
  store.add('任务A');
  store.add('任务B');
  // 清 require 缓存，模拟小程序重启后重新加载模块
  delete require.cache[require.resolve(STORE_PATH)];
  const store2 = require(STORE_PATH);
  const list = store2.load();
  assert.strictEqual(list.length, 2);
  assert.strictEqual(list[0].title, '任务A');
  delete require.cache[require.resolve(STORE_PATH)];
});

test('toggle 切换完成态且幂等', () => {
  store.add('任务');
  assert.strictEqual(store.toggle(1)[0].done, true);
  assert.strictEqual(store.toggle(1)[0].done, false);
});

test('toggle 只影响目标 id', () => {
  store.add('A'); // id 1
  store.add('B'); // id 2
  store.toggle(1);
  const list = store.load();
  assert.strictEqual(list.find((i) => i.id === 1).done, true);
  assert.strictEqual(list.find((i) => i.id === 2).done, false);
});

test('remove 删除指定项', () => {
  store.add('A'); store.add('B'); store.add('C');
  const list = store.remove(2);
  assert.strictEqual(list.length, 2);
  assert.strictEqual(list.some((i) => i.id === 2), false);
});

test('remove 不存在的 id 不报错且列表不变', () => {
  store.add('A');
  assert.strictEqual(store.remove(999).length, 1);
});

test('nextId = 当前最大 id + 1', () => {
  assert.strictEqual(store.nextId([]), 1);
  store.add('A'); store.add('B'); // ids 1,2
  assert.strictEqual(store.nextId(store.load()), 3);
});

console.log('\n' + passed + ' passed, ' + failed + ' failed');
process.exit(failed ? 1 : 0);
