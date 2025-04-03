<template>
  <view class="home-container">
    <!-- 用户信息头部 -->
    <home-header 
      :nickname="userInfo.nickname"
      :avatar="userInfo.avatar"
    />
    
    <!-- 食物识别区域 -->
    <home-scanner 
      :loading="scanning"
      :food-data="foodData"
      :dishes="calorieData?.dishes || []"
      @scan="handleScan"
      @save="handleSave"
    />
    
    <!-- 卡路里建议 -->
    <home-advice 
      v-if="calorieData"
      :calorie-data="calorieData"
    />
    
    <!-- 历史记录按钮 -->
    <view class="history-button" @click="goToHistory">
      <text>历史记录</text>
    </view>
  </view>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import HomeHeader from './components/HomeHeader.vue'
import HomeScanner from './components/HomeScanner.vue'
import HomeAdvice from './components/HomeAdvice.vue'

// 定义组件名称
defineOptions({
  name: 'home'
})

// 用户信息
const userInfo = ref({
  nickname: '测试用户',
  avatar: '/static/logo.png'
})

// 扫描状态
const scanning = ref(false)

// 食物数据
const foodData = ref<{
  image?: string
  weight?: number
} | null>(null)

// 卡路里数据
const calorieData = ref<{
  foods: string[]
  dishes: string[]
  calories: number
  advice: string
} | null>(null)

// 处理扫描
const handleScan = async () => {
  try {
    scanning.value = true
    foodData.value = null
    calorieData.value = null
    
    // TODO: 替换为实际的树莓派数据接收逻辑
    // const response = await uni.request({
    //   url: 'YOUR_RASPBERRY_PI_URL/scan',
    //   method: 'GET',
    //   timeout: 10000 // 10秒超时
    // })
    
    // 模拟接收数据
    await new Promise(resolve => setTimeout(resolve, 2000))
    foodData.value = {
      image: '/static/logo.png',
      weight: 250
    }
    
    // 模拟服务器分析
    await new Promise(resolve => setTimeout(resolve, 1000))
    calorieData.value = {
      foods: ['米饭', '青菜'],
      dishes: ['白米饭', '清炒青菜'],
      calories: 350,
      advice: '您的饮食习惯很健康，卡路里摄入正常，请继续保持该习惯并每日坚持运动。'
    }
    
  } catch (error) {
    console.error('扫描失败：', error)
    uni.showToast({
      title: '处理失败，请重试',
      icon: 'none'
    })
  } finally {
    scanning.value = false
  }
}

// 处理保存
const handleSave = async () => {
  if (!foodData.value || !calorieData.value) return
  
  try {
    // 保存到本地
    const history = uni.getStorageSync('foodHistory') || []
    history.unshift({
      ...foodData.value,
      ...calorieData.value,
      timestamp: new Date().toISOString()
    })
    uni.setStorageSync('foodHistory', history)
    
    // TODO: 上传到云端
    // await uni.request({
    //   url: 'YOUR_API_URL/history',
    //   method: 'POST',
    //   data: {
    //     ...foodData.value,
    //     ...calorieData.value,
    //     timestamp: new Date().toISOString()
    //   }
    // })
    
    uni.showToast({
      title: '保存成功',
      icon: 'success'
    })
    
    // 清空当前数据
    foodData.value = null
    calorieData.value = null
    
  } catch (error) {
    console.error('保存失败：', error)
    uni.showToast({
      title: '保存失败，请重试',
      icon: 'error'
    })
  }
}

// 跳转到历史记录
const goToHistory = () => {
  uni.navigateTo({
    url: '/pages/History'
  })
}
</script>

<style lang="scss">
/* 首页容器样式 */
.home-container {
  min-height: 100vh;
  background-color: #f5f5f5;
  padding: 20px;
  box-sizing: border-box;
}

/* 历史记录按钮样式 */
.history-button {
  position: fixed;
  bottom: 40px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #007AFF;
  color: #fff;
  padding: 12px 24px;
  border-radius: 24px;
  font-size: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}
</style> 