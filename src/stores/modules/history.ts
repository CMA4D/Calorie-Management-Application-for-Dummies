import { defineStore } from 'pinia'
import type { FoodData } from '@/types/food'

interface HistoryState {
  currentDetail: FoodData | null
  historyList: FoodData[]
}

export const useHistoryStore = defineStore('history', {
  state: (): HistoryState => ({
    currentDetail: null,
    historyList: []
  }),

  actions: {
    // 设置当前详情
    setCurrentDetail(data: FoodData) {
      this.currentDetail = data
    },

    // 清除当前详情
    clearCurrentDetail() {
      this.currentDetail = null
    },

    // 加载历史记录
    loadHistory() {
      try {
        const history = uni.getStorageSync('foodHistory') || []
        this.historyList = history
      } catch (error) {
        console.error('加载历史记录失败：', error)
      }
    },

    // 添加历史记录
    addHistory(data: FoodData) {
      try {
        this.historyList.unshift(data)
        uni.setStorageSync('foodHistory', this.historyList)
      } catch (error) {
        console.error('添加历史记录失败：', error)
      }
    },

    // 删除历史记录
    deleteHistory(index: number) {
      try {
        this.historyList.splice(index, 1)
        uni.setStorageSync('foodHistory', this.historyList)
      } catch (error) {
        console.error('删除历史记录失败：', error)
      }
    },

    // 计算平均卡路里
    calculateAverageCalories() {
      if (this.historyList.length === 0) return 0
      
      const totalCalories = this.historyList.reduce((sum, item) => sum + item.calories, 0)
      return Math.round(totalCalories / this.historyList.length)
    }
  }
}) 