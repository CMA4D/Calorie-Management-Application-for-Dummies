<template>
  <view class="register-container">
    <!-- 注册头部 -->
    <RegisterHeader />
    
    <!-- 注册表单 -->
    <RegisterForm 
      :loading="loading"
      @submit="handleSubmit"
    />
    
    <!-- 注册页脚 -->
    <RegisterFooter />
    
    <!-- 测试按钮 -->
    <view class="debug-buttons" v-if="isDevelopment">
      <button @click="simulateEmailExists">模拟邮箱已存在</button>
      <button @click="simulateUsernameExists">模拟用户名已存在</button>
      <button @click="simulateNetworkError">模拟网络错误</button>
    </view>
  </view>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useUserStore } from '@/stores/modules/user'
import RegisterHeader from '@/components/auth/register/RegisterHeader.vue'
import RegisterForm from '@/components/auth/register/RegisterForm.vue'
import RegisterFooter from '@/components/auth/register/RegisterFooter.vue'

// 定义组件名称
defineOptions({
  name: 'Register'
})

// 用户状态管理
const userStore = useUserStore()

// 加载状态
const loading = ref(false)

// 是否为开发环境
const isDevelopment = process.env.NODE_ENV === 'development'

// 处理表单提交
const handleSubmit = async (data: { username: string; password: string; confirmPassword: string; email: string }) => {
  try {
    loading.value = true
    
    // 注册
    const success = await userStore.register(data)
    
    if (success) {
      uni.showToast({
        title: '注册成功',
        icon: 'success'
      })
      
      // 延迟返回登录页
      setTimeout(() => {
        uni.navigateBack()
      }, 1500)
    } else {
      uni.showToast({
        title: '注册失败，请重试',
        icon: 'error'
      })
    }
  } catch (error) {
    console.error('注册失败：', error)
    uni.showToast({
      title: '注册失败，请重试',
      icon: 'error'
    })
  } finally {
    loading.value = false
  }
}

// 模拟邮箱已存在
const simulateEmailExists = () => {
  uni.showToast({
    title: '该邮箱已被注册',
    icon: 'none'
  })
}

// 模拟用户名已存在
const simulateUsernameExists = () => {
  uni.showToast({
    title: '该用户名已被使用',
    icon: 'none'
  })
}

// 模拟网络错误
const simulateNetworkError = () => {
  uni.showToast({
    title: '网络连接失败',
    icon: 'error'
  })
}
</script>

<style lang="scss">
/* 注册页面容器样式 */
.register-container {
  min-height: 100vh;
  background-color: #f5f5f5;
  padding: 20px;
  box-sizing: border-box;
}

/* 调试按钮组样式 */
.debug-buttons {
  margin-top: 20px;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  
  button {
    margin-bottom: 10px;
    background-color: #f0f0f0;
    color: #666;
    
    &:last-child {
      margin-bottom: 0;
    }
  }
}
</style> 