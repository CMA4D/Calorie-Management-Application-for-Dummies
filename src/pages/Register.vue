<template>
  <view class="register-container">
    <!-- 注册头部 -->
    <register-header />
    
    <!-- 注册表单 -->
    <register-form 
      :loading="loading"
      @submit="handleRegister"
    />
    
    <!-- 注册页脚 -->
    <register-footer />
  </view>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import RegisterHeader from './components/RegisterHeader.vue'
import RegisterForm from './components/RegisterForm.vue'
import RegisterFooter from './components/RegisterFooter.vue'

// 定义组件名称
defineOptions({
  name: 'register'
})

// 加载状态
const loading = ref(false)

// 处理注册提交
const handleRegister = async (data: {
  username: string
  password: string
  confirmPassword: string
  email: string
}) => {
  try {
    loading.value = true
    
    // TODO: 调用注册 API
    console.log('注册数据：', data)
    
    // 模拟注册成功
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    // 注册成功后跳转到登录页
    uni.showToast({
      title: '注册成功',
      icon: 'success'
    })
    
    setTimeout(() => {
      uni.navigateBack()
    }, 1500)
    
  } catch (error) {
    console.error('注册失败：', error)
    uni.showToast({
      title: '注册失败',
      icon: 'error'
    })
  } finally {
    loading.value = false
  }
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
</style> 