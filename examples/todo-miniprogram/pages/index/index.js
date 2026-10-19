// pages/index/index.js
const store = require('../../utils/store.js');

Page({
  data: {
    todos: [],
    input: ''
  },

  onShow() {
    this.refresh();
  },

  refresh() {
    this.setData({ todos: store.load() });
  },

  onInput(e) {
    this.setData({ input: e.detail.value });
  },

  add() {
    const title = this.data.input.trim();
    if (!title) {
      return;
    }
    store.add(title);
    this.setData({ input: '' });
    this.refresh();
  },

  toggle(e) {
    const id = Number(e.currentTarget.dataset.id);
    store.toggle(id);
    this.refresh();
  },

  remove(e) {
    const id = Number(e.currentTarget.dataset.id);
    store.remove(id);
    this.refresh();
  }
});
