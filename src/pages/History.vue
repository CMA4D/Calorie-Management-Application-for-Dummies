<template>
  <view class="history-container">
    <!-- 历史记录头部 -->
    <view class="history-header">
      <view class="back-button" @click="handleBack">
        <text class="iconfont icon-back">←</text>
      </view>
      <text class="title">历史记录</text>
    </view>
    
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
      @refresherrefresh="handleRefresh"
    >
      <!-- 加载状态 -->
      <view v-if="loading" class="loading">
        <text>数据更新中...</text>
      </view>
      
      <!-- 更新失败 -->
      <view v-else-if="loadError" class="error">
        <text>更新失败，请重试</text>
        <button class="retry-button" @click="handleRefresh">重试</button>
      </view>
      
      <!-- 空状态 -->
      <view v-else-if="historyList.length === 0" class="empty">
        <text>暂无历史记录</text>
      </view>
      
      <!-- 历史记录列表 -->
      <view v-else class="list">
        <view 
          v-for="(item, index) in historyList" 
          :key="index"
          class="history-item"
          @click="goToDetail(item)"
        >
          <!-- 食物图片 -->
          <image 
            class="food-image" 
            :src="item.image" 
            mode="aspectFill"
          />
          
          <!-- 食物信息 -->
          <view class="food-info">
            <!-- 菜品列表 -->
            <view class="dishes">
              <text 
                v-for="(dish, dishIndex) in item.dishes" 
                :key="dishIndex"
                class="dish-item"
              >
                {{ dish }}
              </text>
            </view>
            
            <!-- 卡路里值 -->
            <text class="calories">{{ item.calories }} 千卡</text>
            
            <!-- 时间 -->
            <text class="time">{{ formatTime(item.timestamp) }}</text>
          </view>
          
          <!-- 删除按钮 -->
          <view class="delete-button" @click.stop="handleDelete(item)">
            <text class="iconfont icon-delete">×</text>
          </view>
        </view>
      </view>
    </scroll-view>
  </view>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'

// 定义组件名称
defineOptions({
  name: 'history'
})

// 历史记录列表
const historyList = ref<Array<{
  image: string
  weight: number
  foods: string[]
  dishes: string[]
  calories: number
  timestamp: string
}>>([])

// 加载状态
const loading = ref(false)

// 刷新状态
const refreshing = ref(false)

// 加载错误
const loadError = ref(false)

// 计算平均卡路里
const averageCalories = computed(() => {
  if (historyList.value.length === 0) {
    return '缺少样本暂无均值'
  }
  
  // 确保卡路里值为数字类型
  const validHistory = historyList.value.filter((item: typeof historyList.value[0]) => {
    const calories = Number(item.calories)
    return !isNaN(calories)
  })
  
  if (validHistory.length === 0) {
    return '缺少样本暂无均值'
  }
  
  // 取最近10条或全部记录
  const recentHistory = validHistory.slice(0, 10)
  const total = recentHistory.reduce((sum, item) => sum + Number(item.calories), 0)
  const average = Math.round(total / recentHistory.length)
  
  return `${average} 千卡`
})

// 处理返回
const handleBack = () => {
  uni.navigateBack()
}

// 处理刷新
const handleRefresh = async () => {
  try {
    refreshing.value = true
    loading.value = true
    loadError.value = false
    
    // 读取本地数据
    const localHistory = uni.getStorageSync('foodHistory') || []
    // 确保卡路里值为数字类型
    historyList.value = localHistory.map((item: typeof historyList.value[0]) => ({
      ...item,
      calories: Number(item.calories)
    }))
    
    // TODO: 从服务器同步数据
    // const response = await uni.request({
    //   url: 'YOUR_API_URL/history',
    //   method: 'GET',
    //   timeout: 10000
    // })
    
    // 模拟服务器请求
    await new Promise(resolve => setTimeout(resolve, 2000))
    
  } catch (error) {
    console.error('同步失败：', error)
    loadError.value = true
  } finally {
    loading.value = false
    refreshing.value = false
  }
}

// 跳转到详情页
const goToDetail = (item: typeof historyList.value[0]) => {
  uni.navigateTo({
    url: `/pages/HistoryDetail?data=${encodeURIComponent(JSON.stringify(item))}`
  })
}

// 格式化时间
const formatTime = (timestamp: string) => {
  const date = new Date(timestamp)
  return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')} ${String(date.getHours()).padStart(2, '0')}:${String(date.getMinutes()).padStart(2, '0')}`
}

// 处理删除
const handleDelete = async (item: typeof historyList.value[0]) => {
  try {
    // 显示确认对话框
    const result = await uni.showModal({
      title: '确认删除',
      content: '确定要删除这条记录吗？',
      confirmText: '删除',
      confirmColor: '#ff3b30'
    })
    
    if (!result.confirm) return
    
    // 从本地存储中删除
    const localHistory = uni.getStorageSync('foodHistory') || []
    const newHistory = localHistory.filter((record: typeof historyList.value[0]) => record.timestamp !== item.timestamp)
    uni.setStorageSync('foodHistory', newHistory)
    
    // 更新列表
    historyList.value = newHistory.map((item: typeof historyList.value[0]) => ({
      ...item,
      calories: Number(item.calories)
    }))
    
    // TODO: 同步删除到服务器
    // await uni.request({
    //   url: 'YOUR_API_URL/history',
    //   method: 'DELETE',
    //   data: {
    //     timestamp: item.timestamp
    //   }
    // })
    
    uni.showToast({
      title: '删除成功',
      icon: 'success'
    })
    
  } catch (error) {
    console.error('删除失败：', error)
    uni.showToast({
      title: '删除失败，请重试',
      icon: 'error'
    })
  }
}

// 页面加载时读取本地数据
onMounted(() => {
  const localHistory = uni.getStorageSync('foodHistory') || []
  // 确保卡路里值为数字类型
  historyList.value = localHistory.map((item: typeof historyList.value[0]) => ({
    ...item,
    calories: Number(item.calories)
  }))
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

/* 历史记录头部样式 */
.history-header {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
  
  /* 返回按钮样式 */
  .back-button {
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 10px;
    
    .icon-back {
      font-size: 24px;
      color: #333;
    }
  }
  
  /* 标题样式 */
  .title {
    font-size: 24px;
    font-weight: bold;
    color: #333;
  }
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
  
  /* 历史记录项样式 */
  .history-item {
    background-color: #fff;
    border-radius: 8px;
    margin-bottom: 15px;
    overflow: hidden;
    display: flex;
    position: relative;
    
    /* 食物图片样式 */
    .food-image {
      width: 100px;
      height: 100px;
    }
    
    /* 食物信息样式 */
    .food-info {
      flex: 1;
      padding: 15px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      
      /* 菜品列表样式 */
      .dishes {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        
        .dish-item {
          background-color: #f0f0f0;
          color: #333;
          padding: 4px 12px;
          border-radius: 12px;
          font-size: 14px;
        }
      }
      
      /* 卡路里值样式 */
      .calories {
        font-size: 16px;
        color: #333;
        font-weight: bold;
      }
      
      /* 时间样式 */
      .time {
        font-size: 12px;
        color: #999;
      }
    }
    
    /* 删除按钮样式 */
    .delete-button {
      position: absolute;
      top: 10px;
      right: 10px;
      width: 30px;
      height: 30px;
      background-color: rgba(255, 59, 48, 0.1);
      border-radius: 15px;
      display: flex;
      align-items: center;
      justify-content: center;
      
      .icon-delete {
        font-size: 20px;
        color: #ff3b30;
      }
    }
  }
}
</style> 