<template>
  <view class="history-container">
    <!-- 页面头部 -->
    <page-header title="历史记录" />
    
    <!-- 平均卡路里 -->
    <view class="average-calories">
      <text class="label">近日摄入平均卡路里</text>
      <text class="value">{{ averageCalories }}</text>
    </view>
    
    <!-- 历史记录列表 -->
    <scroll-view 
      class="history-list"
      scroll-y
      refresher-enabled
      :refresher-triggered="refreshing"
      @refresherrefresh="loadHistory"
    >
      <!-- 加载状态 -->
      <view v-if="loading" class="loading">
        <text>数据更新中...</text>
      </view>
      
      <!-- 更新失败 -->
      <view v-else-if="loadError" class="error">
        <text>更新失败，请重试</text>
        <button class="retry-button" @click="loadHistory">重试</button>
      </view>
      
      <!-- 空状态 -->
      <view v-else-if="historyList.length === 0" class="empty">
        <text>暂无历史记录</text>
      </view>
      
      <!-- 历史记录列表 -->
      <view v-else class="list">
        <history-item
          v-for="(item, index) in historyList"
          :key="index"
          :data="item"
          :index="index"
          @click="handleViewDetail"
          @delete="handleDelete"
        />
      </view>
    </scroll-view>
  </view>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import PageHeader from '@/components/common/layout/PageHeader.vue'
import HistoryItem from '@/components/business/history/HistoryItem.vue'
import { useFoodHistory } from '@/hooks/useFoodHistory'
import { useHistoryStore } from '@/stores/modules/history'
import type { FoodData } from '@/types/food'

// 定义组件名称
defineOptions({
  name: 'History'
})

// 使用食物历史记录 hook
const {
  historyList,
  loading,
  refreshing,
  loadError,
  averageCalories,
  loadHistory,
  deleteHistory
} = useFoodHistory()

// 历史记录状态管理
const historyStore = useHistoryStore()

// 当前详情
const currentDetail = ref<any>(null)

// 处理查看详情
const handleViewDetail = (detail: FoodData) => {
  historyStore.setCurrentDetail(detail)
  uni.navigateTo({
    url: '/pages/history/HistoryDetail'
  })
}

// 处理删除记录
const handleDelete = (index: number) => {
  uni.showModal({
    title: '提示',
    content: '确定要删除这条记录吗？',
    success: (res) => {
      if (res.confirm) {
        deleteHistory(index)
      }
    }
  })
}

// 处理下拉刷新
const handleRefresh = async () => {
  refreshing.value = true
  await loadHistory()
}

// 页面加载时加载历史记录
onMounted(() => {
  loadHistory()
})
</script>

<style lang="scss">
/* 历史记录页面容器样式 */
.history-container {
  min-height: 100vh;
  background-color: #f5f5f5;
  padding: 20px;
  box-sizing: border-box;
}

/* 平均卡路里样式 */
.average-calories {
  background-color: #fff;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  
  .label {
    font-size: 14px;
    color: #666;
    margin-bottom: 8px;
  }
  
  .value {
    font-size: 24px;
    color: #333;
    font-weight: bold;
  }
}

/* 历史记录列表样式 */
.history-list {
  height: calc(100vh - 200px);
  
  /* 加载状态样式 */
  .loading {
    padding: 20px;
    text-align: center;
    color: #666;
  }
  
  /* 错误状态样式 */
  .error {
    padding: 20px;
    text-align: center;
    color: #666;
    
    .retry-button {
      margin-top: 10px;
      background-color: #007AFF;
      color: #fff;
      padding: 8px 16px;
      border-radius: 4px;
      font-size: 14px;
    }
  }
  
  /* 空状态样式 */
  .empty {
    padding: 40px 20px;
    text-align: center;
    color: #999;
  }
  
  /* 列表样式 */
  .list {
    padding: 0 0 20px;
  }
}
</style> 