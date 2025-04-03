<template>
  <view class="login-container">
    <!-- 登录页面头部 -->
    <LoginHeader />
    
    <!-- 登录表单 -->
    <LoginForm 
      :loading="loading"
      @submit="handleLogin"
    />
    
    <!-- 登录页面底部 -->
    <LoginFooter />

    <!-- 调试按钮组 -->
    <view class="debug-buttons" v-if="isDevelopment">
      <button @click="simulateLoginSuccess">模拟登录成功</button>
      <button @click="simulateUserNotExist">模拟用户不存在</button>
      <button @click="simulatePasswordError">模拟密码错误</button>
    </view>
  </view>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import LoginHeader from './components/LoginHeader.vue'
import LoginForm from './components/LoginForm.vue'
import LoginFooter from './components/LoginFooter.vue'

// 定义组件名称
defineOptions({
  name: 'login'
})

// 登录加载状态
const loading = ref(false)

// 是否为开发环境
const isDevelopment = process.env.NODE_ENV === 'development'

// 处理登录逻辑
const handleLogin = async (formData: { username: string; password: string }) => {
  try {
    loading.value = true
    // TODO: 实现实际的登录逻辑
    console.log('登录信息：', formData)
    
    // 模拟登录延迟
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    // 登录成功后跳转
    uni.showToast({
      title: '登录成功',
      icon: 'success'
    })
    
    // 暂时注释掉跳转，等待主页创建完成
    // uni.reLaunch({
    //   url: '/pages/Home'
    // })
  } catch (error) {
    console.error('登录失败：', error)
    uni.showToast({
      title: '登录失败，请稍后重试',
      icon: 'error'
    })
  } finally {
    loading.value = false
  }
}

// 模拟登录成功
const simulateLoginSuccess = async () => {
  loading.value = true
  await new Promise(resolve => setTimeout(resolve, 1000))
  uni.showToast({
    title: '登录成功',
    icon: 'success'
  })
  setTimeout(() => {
    uni.reLaunch({
      url: '/pages/Home'
    })
  }, 1500)
  loading.value = false
}

// 模拟用户不存在
const simulateUserNotExist = () => {
  uni.showModal({
    title: '提示',
    content: '用户名错误，该用户不存在',
    showCancel: false,
    success: () => {
      // 可以选择跳转到注册页面
      uni.navigateTo({
        url: '/pages/Register'
      })
    }
  })
}

// 模拟密码错误
const simulatePasswordError = () => {
  uni.showModal({
    title: '提示',
    content: '用户名或密码错误',
    confirmText: '找回密码',
    cancelText: '重试',
    success: (res) => {
      if (res.confirm) {
        uni.navigateTo({
          url: '/pages/ResetPassword'
        })
      }
    }
  })
}
</script>

<style lang="scss">
/* 登录页面容器样式 */
.login-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f5f5f5;
  padding: 20px;
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