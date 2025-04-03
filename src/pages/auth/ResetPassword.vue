<template>
  <view class="reset-password-container">
    <!-- 找回密码头部 -->
    <ResetPasswordHeader />
    
    <!-- 找回密码表单 -->
    <ResetPasswordForm 
      :loading="loading"
      @submit="handleSubmit"
      @send-code="handleSendCode"
    />
    
    <!-- 找回密码页脚 -->
    <ResetPasswordFooter />
    
    <!-- 测试按钮 -->
    <view class="debug-buttons" v-if="isDevelopment">
      <button @click="simulateEmailNotFound">模拟邮箱未注册</button>
      <button @click="simulateCodeExpired">模拟验证码过期</button>
      <button @click="simulateCodeError">模拟验证码错误</button>
      <button @click="simulateNetworkError">模拟网络错误</button>
    </view>
  </view>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useUserStore } from '@/stores/modules/user'
import ResetPasswordHeader from '@/components/auth/reset-password/ResetPasswordHeader.vue'
import ResetPasswordForm from '@/components/auth/reset-password/ResetPasswordForm.vue'
import ResetPasswordFooter from '@/components/auth/reset-password/ResetPasswordFooter.vue'

// 定义组件名称
defineOptions({
  name: 'ResetPassword'
})

// 用户状态管理
const userStore = useUserStore()

// 加载状态
const loading = ref(false)

// 是否为开发环境
const isDevelopment = process.env.NODE_ENV === 'development'

// 处理发送验证码
const handleSendCode = async (email: string) => {
  try {
    loading.value = true
    
    // 发送验证码
    const success = await userStore.resetPassword(email)
    
    if (success) {
      uni.showToast({
        title: '验证码已发送',
        icon: 'success'
      })
    } else {
      uni.showToast({
        title: '该邮箱未注册',
        icon: 'none'
      })
    }
  } catch (error) {
    console.error('发送验证码失败：', error)
    uni.showToast({
      title: '发送失败，请重试',
      icon: 'error'
    })
  } finally {
    loading.value = false
  }
}

// 处理表单提交
const handleSubmit = async (data: { email: string; code: string; newPassword: string; confirmPassword: string }) => {
  try {
    loading.value = true
    
    // TODO: 验证验证码并重置密码
    // const success = await userStore.verifyCodeAndResetPassword(data)
    
    // 模拟验证成功
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    uni.showToast({
      title: '密码重置成功',
      icon: 'success'
    })
    
    // 延迟返回登录页
    setTimeout(() => {
      uni.navigateBack()
    }, 1500)
  } catch (error) {
    console.error('重置密码失败：', error)
    uni.showToast({
      title: '重置失败，请重试',
      icon: 'error'
    })
  } finally {
    loading.value = false
  }
}

// 模拟邮箱未注册
const simulateEmailNotFound = () => {
  uni.showToast({
    title: '该邮箱未注册',
    icon: 'none'
  })
}

// 模拟验证码过期
const simulateCodeExpired = () => {
  uni.showToast({
    title: '验证码已过期',
    icon: 'none'
  })
}

// 模拟验证码错误
const simulateCodeError = () => {
  uni.showToast({
    title: '验证码错误',
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
/* 找回密码页面容器样式 */
.reset-password-container {
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