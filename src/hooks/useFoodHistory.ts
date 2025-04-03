import { ref, computed } from 'vue'
import { useHistoryStore } from '@/stores/modules/history'
import type { FoodData } from '@/types/food'

// 食物历史记录 hook
export function useFoodHistory() {
  const historyStore = useHistoryStore()
  
  // 历史记录列表
  const historyList = computed(() => historyStore.historyList)
  
  // 加载状态
  const loading = ref(false)
  
  // 刷新状态
  const refreshing = ref(false)
  
  // 错误状态
  const loadError = ref<string | null>(null)
  
  // 平均卡路里
  const averageCalories = computed(() => historyStore.calculateAverageCalories())
  
  // 加载历史记录
  const loadHistory = async () => {
    try {
      loading.value = true
      loadError.value = null
      await historyStore.loadHistory()
    } catch (error) {
      console.error('加载历史记录失败：', error)
      loadError.value = '加载失败，请重试'
    } finally {
      loading.value = false
      refreshing.value = false
    }
  }
  
  // 添加历史记录
  const addHistory = async (data: FoodData) => {
    try {
      await historyStore.addHistory(data)
    } catch (error) {
      console.error('添加历史记录失败：', error)
      throw error
    }
  }
  
  // 删除历史记录
  const deleteHistory = (index: number) => {
    uni.showModal({
      title: '提示',
      content: '确定要删除这条记录吗？',
      success: (res) => {
        if (res.confirm) {
          historyStore.deleteHistory(index)
        }
      }
    })
  }
  
  return {
    historyList,
    loading,
    refreshing,
    loadError,
    averageCalories,
    loadHistory,
    addHistory,
    deleteHistory
  }
} 