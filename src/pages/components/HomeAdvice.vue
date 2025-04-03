<template>
  <view class="home-advice">
    <!-- 食材列表 -->
    <view class="foods-list">
      <text class="label">识别到的食材：</text>
      <view class="foods">
        <text 
          v-for="(food, index) in calorieData.foods" 
          :key="index"
          class="food-item"
        >
          {{ food }}
        </text>
      </view>
    </view>
    
    <!-- 卡路里值 -->
    <view class="calories">
      <text class="label">预计卡路里：</text>
      <text class="value">{{ calorieData.calories }} 千卡</text>
    </view>
    
    <!-- 建议内容 -->
    <view class="advice-content">
      <text class="icon">💡</text>
      <text class="text">{{ calorieData.advice }}</text>
    </view>
  </view>
</template>

<script setup lang="ts">
// 定义组件名称
defineOptions({
  name: 'homeAdvice'
})

// 定义组件属性
interface Props {
  calorieData: {
    foods: string[]
    calories: number
    advice: string
  }
}

defineProps<Props>()
</script>

<style lang="scss">
/* 卡路里建议组件样式 */
.home-advice {
  background-color: #fff;
  border-radius: 8px;
  padding: 20px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  
  /* 食材列表样式 */
  .foods-list {
    margin-bottom: 15px;
    
    .label {
      font-size: 14px;
      color: #666;
      margin-bottom: 8px;
      display: block;
    }
    
    .foods {
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
  }
  
  /* 卡路里值样式 */
  .calories {
    margin-bottom: 15px;
    
    .label {
      font-size: 14px;
      color: #666;
      margin-right: 8px;
    }
    
    .value {
      font-size: 16px;
      color: #333;
      font-weight: bold;
    }
  }
  
  /* 建议内容样式 */
  .advice-content {
    background-color: #f8f8f8;
    border-radius: 8px;
    padding: 15px;
    display: flex;
    align-items: flex-start;
    
    .icon {
      font-size: 20px;
      margin-right: 10px;
    }
    
    .text {
      flex: 1;
      font-size: 14px;
      color: #333;
      line-height: 1.5;
    }
  }
}
</style> 