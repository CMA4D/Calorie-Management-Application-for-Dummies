<template>
  <view class="detail-container">
    <!-- 详情页头部 -->
    <view class="detail-header">
      <view class="back-button" @click="handleBack">
        <text class="iconfont icon-back">←</text>
      </view>
      <text class="title">记录详情</text>
    </view>
    
    <!-- 食物图片 -->
    <view class="food-image-container">
      <image 
        class="food-image" 
        :src="detailData.image" 
        mode="aspectFill"
      />
    </view>
    
    <!-- 食物信息 -->
    <view class="food-info">
      <!-- 重量信息 -->
      <view class="info-item">
        <text class="label">重量</text>
        <text class="value">{{ detailData.weight }}g</text>
      </view>
      
      <!-- 卡路里信息 -->
      <view class="info-item">
        <text class="label">卡路里</text>
        <text class="value">{{ detailData.calories }} 千卡</text>
      </view>
      
      <!-- 识别到的食物 -->
      <view class="info-item">
        <text class="label">识别到的食物</text>
        <view class="food-list">
          <text 
            v-for="(food, index) in detailData.foods" 
            :key="index"
            class="food-item"
          >
            {{ food }}
          </text>
        </view>
      </view>
      
      <!-- 菜品列表 -->
      <view class="info-item">
        <text class="label">菜品列表</text>
        <view class="dish-list">
          <text 
            v-for="(dish, index) in detailData.dishes" 
            :key="index"
            class="dish-item"
          >
            {{ dish }}
          </text>
        </view>
      </view>
      
      <!-- 记录时间 -->
      <view class="info-item">
        <text class="label">记录时间</text>
        <text class="value">{{ formatTime(detailData.timestamp) }}</text>
      </view>
    </view>
  </view>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

// 定义组件名称
defineOptions({
  name: 'historyDetail'
})

// 详情数据
const detailData = ref<{
  image: string
  weight: number
  foods: string[]
  dishes: string[]
  calories: number
  timestamp: string
}>({
  image: '',
  weight: 0,
  foods: [],
  dishes: [],
  calories: 0,
  timestamp: ''
})

// 处理返回
const handleBack = () => {
  uni.navigateBack()
}

// 格式化时间
const formatTime = (timestamp: string) => {
  const date = new Date(timestamp)
  return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')} ${String(date.getHours()).padStart(2, '0')}:${String(date.getMinutes()).padStart(2, '0')}`
}

// 页面加载时获取详情数据
onMounted(() => {
  const pages = getCurrentPages()
  const currentPage = pages[pages.length - 1]
  const data = currentPage.$page?.options?.data
  
  if (data) {
    try {
      detailData.value = JSON.parse(decodeURIComponent(data))
    } catch (error) {
      console.error('解析详情数据失败：', error)
      uni.showToast({
        title: '数据加载失败',
        icon: 'none'
      })
    }
  }
})
</script>

<style lang="scss">
/* 详情页容器样式 */
.detail-container {
  min-height: 100vh;
  background-color: #f5f5f5;
  padding: 20px;
  box-sizing: border-box;
}

/* 详情页头部样式 */
.detail-header {
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

/* 食物图片容器样式 */
.food-image-container {
  background-color: #fff;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 20px;
  display: flex;
  justify-content: center;
  
  /* 食物图片样式 */
  .food-image {
    width: 200px;
    height: 200px;
    border-radius: 8px;
  }
}

/* 食物信息样式 */
.food-info {
  background-color: #fff;
  border-radius: 8px;
  padding: 20px;
  
  /* 信息项样式 */
  .info-item {
    margin-bottom: 20px;
    
    &:last-child {
      margin-bottom: 0;
    }
    
    /* 标签样式 */
    .label {
      font-size: 14px;
      color: #666;
      margin-bottom: 8px;
      display: block;
    }
    
    /* 值样式 */
    .value {
      font-size: 16px;
      color: #333;
      font-weight: bold;
    }
    
    /* 食物列表样式 */
    .food-list {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      
      .food-item {
        background-color: #f0f0f0;
        color: #333;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 14px;
      }
    }
    
    /* 菜品列表样式 */
    .dish-list {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      
      .dish-item {
        background-color: #e6f3ff;
        color: #007AFF;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 14px;
      }
    }
  }
}
</style> 