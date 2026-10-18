// utils/store.js — 待办数据持久化（基于微信本地 Storage）
const KEY = 'todos';

function load() {
  return wx.getStorageSync(KEY) || [];
}

function save(list) {
  wx.setStorageSync(KEY, list);
}

function nextId(list) {
  return list.reduce((max, it) => Math.max(max, it.id), 0) + 1;
}

function add(title) {
  const list = load();
  const item = { id: nextId(list), title: title.trim(), done: false };
  list.push(item);
  save(list);
  return item;
}

function toggle(id) {
  const list = load().map((it) =>
    it.id === id ? Object.assign({}, it, { done: !it.done }) : it
  );
  save(list);
  return list;
}

function remove(id) {
  const list = load().filter((it) => it.id !== id);
  save(list);
  return list;
}

module.exports = { load, save, nextId, add, toggle, remove };
