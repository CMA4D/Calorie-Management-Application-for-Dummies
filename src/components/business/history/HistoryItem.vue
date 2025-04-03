<template>
  <view class="history-item" @click="handleClick">
    <!-- 食物图片 -->
    <image 
      class="food-image" 
      :src="data.image" 
      mode="aspectFill"
    />
    
    <!-- 食物信息 -->
    <view class="food-info">
      <!-- 菜品列表 -->
      <view class="dishes">
        <text 
          v-for="(dish, index) in data.dishes" 
          :key="index"
          class="dish-item"
        >
          {{ dish }}
        </text>
      </view>
      
      <!-- 卡路里值 -->
      <text class="calories">{{ data.calories }} 千卡</text>
      
      <!-- 时间 -->
      <text class="time">{{ formatTime(data.timestamp) }}</text>
    </view>
    
    <!-- 删除按钮 -->
    <view class="delete-button" @click.stop="handleDelete">
      <text class="iconfont icon-delete">×</text>
    </view>
  </view>
</template>

<script setup lang="ts">
import type { FoodData } from '@/types/food'

// 定义组件名称
defineOptions({
  name: 'historyItem'
})

// 定义属性
const props = defineProps<{
  data: FoodData
  index: number
}>()

// 定义事件
const emit = defineEmits<{
  (e: 'click', data: FoodData): void
  (e: 'delete', index: number): void
}>()

// 处理点击
const handleClick = () => {
  emit('click', props.data)
}

// 处理删除
const handleDelete = () => {
  emit('delete', props.index)
}

// 格式化时间
const formatTime = (timestamp: string) => {
  const date = new Date(timestamp)
  return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')} ${String(date.getHours()).padStart(2, '0')}:${String(date.getMinutes()).padStart(2, '0')}`
}
</script>

<style lang="scss">
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
</style> 