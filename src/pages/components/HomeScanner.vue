<template>
  <view class="scanner-container">
    <!-- 扫描状态 -->
    <view v-if="loading" class="loading">
      <text>正在处理中...</text>
    </view>
    
    <!-- 食物数据 -->
    <view v-else-if="foodData" class="food-data">
      <!-- 食物图片 -->
      <image 
        class="food-image" 
        :src="foodData.image" 
        mode="aspectFill"
      />
      
      <!-- 食物信息 -->
      <view class="food-info">
        <!-- 重量信息 -->
        <text class="weight">{{ foodData.weight }}g</text>
        
        <!-- 菜品列表 -->
        <view v-if="dishes.length > 0" class="dishes">
          <text 
            v-for="(dish, index) in dishes" 
            :key="index"
            class="dish-item"
          >
            {{ dish }}
          </text>
        </view>
        
        <!-- 操作按钮 -->
        <view class="actions">
          <button 
            class="scan-button" 
            @click="handleScan"
          >
            重新扫描
          </button>
          <button 
            class="save-button" 
            @click="handleSave"
          >
            保存记录
          </button>
        </view>
      </view>
    </view>
    
    <!-- 空状态 -->
    <view v-else class="empty">
      <button 
        class="scan-button" 
        @click="handleScan"
      >
        开始扫描
      </button>
    </view>
  </view>
</template>

<script setup lang="ts">
import { ref } from 'vue'

// 定义组件名称
defineOptions({
  name: 'homeScanner'
})

// 定义属性
const props = defineProps<{
  loading: boolean
  foodData: {
    image?: string
    weight?: number
  } | null
  dishes: string[]
}>()

// 定义事件
const emit = defineEmits<{
  (e: 'scan'): void
  (e: 'save'): void
}>()

// 处理扫描
const handleScan = () => {
  emit('scan')
}

// 处理保存
const handleSave = () => {
  emit('save')
}
</script>

<style lang="scss">
/* 扫描容器样式 */
.scanner-container {
  background-color: #fff;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
  
  /* 加载状态样式 */
  .loading {
    height: 200px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #666;
  }
  
  /* 食物数据样式 */
  .food-data {
    display: flex;
    gap: 20px;
    
    /* 食物图片样式 */
    .food-image {
      width: 120px;
      height: 120px;
      border-radius: 8px;
    }
    
    /* 食物信息样式 */
    .food-info {
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      
      /* 重量信息样式 */
      .weight {
        font-size: 18px;
        color: #333;
        font-weight: bold;
      }
      
      /* 菜品列表样式 */
      .dishes {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin: 10px 0;
        
        .dish-item {
          background-color: #f0f0f0;
          color: #333;
          padding: 4px 12px;
          border-radius: 12px;
          font-size: 14px;
        }
      }
      
      /* 操作按钮样式 */
      .actions {
        display: flex;
        gap: 10px;
        
        button {
          flex: 1;
          height: 36px;
          border-radius: 18px;
          font-size: 14px;
          display: flex;
          align-items: center;
          justify-content: center;
          
          &.scan-button {
            background-color: #f0f0f0;
            color: #333;
          }
          
          &.save-button {
            background-color: #007AFF;
            color: #fff;
          }
        }
      }
    }
  }
  
  /* 空状态样式 */
  .empty {
    height: 200px;
    display: flex;
    align-items: center;
    justify-content: center;
    
    .scan-button {
      background-color: #007AFF;
      color: #fff;
      padding: 12px 24px;
      border-radius: 24px;
      font-size: 16px;
    }
  }
}
</style> 