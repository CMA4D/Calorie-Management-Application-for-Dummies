<template>
  <view class="reset-password-container">
    <!-- 找回密码头部 -->
    <reset-password-header />
    
    <!-- 找回密码表单 -->
    <reset-password-form 
      :loading="loading"
      @submit="handleResetPassword"
    />
    
    <!-- 找回密码页脚 -->
    <reset-password-footer />

    <!-- 调试按钮 -->
    <view class="debug-buttons" v-if="isDevelopment">
      <button @click="simulateEmailSent">模拟邮件发送成功</button>
      <button @click="simulateEmailNotFound">模拟邮箱不存在</button>
    </view>
  </view>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import ResetPasswordHeader from './components/ResetPasswordHeader.vue'
import ResetPasswordForm from './components/ResetPasswordForm.vue'
import ResetPasswordFooter from './components/ResetPasswordFooter.vue'

// 定义组件名称
defineOptions({
  name: 'resetPassword'
})

// 加载状态
const loading = ref(false)

// 是否为开发环境
const isDevelopment = process.env.NODE_ENV === 'development'

// 处理找回密码提交
const handleResetPassword = async (data: { email: string }) => {
  try {
    loading.value = true
    
    // TODO: 替换为实际的服务器请求
    // const response = await uni.request({
    //   url: 'YOUR_API_URL/reset-password',
    //   method: 'POST',
    //   data: {
    //     email: data.email
    //   }
    // })
    
    // if (response.statusCode === 200) {
    //   const { code, message } = response.data
    //   if (code === 0) {
    //     uni.showToast({
    //       title: '新密码已发送到您的邮箱',
    //       icon: 'success'
    //     })
    //     setTimeout(() => {
    //       uni.navigateBack()
    //     }, 1500)
    //   } else {
    //     uni.showToast({
    //       title: message,
    //       icon: 'none'
    //     })
    //   }
    // }
    
    // 模拟发送成功
    await new Promise(resolve => setTimeout(resolve, 1000))
    uni.showToast({
      title: '新密码已发送到您的邮箱',
      icon: 'success'
    })
    setTimeout(() => {
      uni.navigateBack()
    }, 1500)
    
  } catch (error) {
    console.error('找回密码失败：', error)
    uni.showToast({
      title: '找回密码失败，请稍后重试',
      icon: 'error'
    })
  } finally {
    loading.value = false
  }
}

// 模拟邮件发送成功
const simulateEmailSent = async () => {
  loading.value = true
  await new Promise(resolve => setTimeout(resolve, 1000))
  uni.showToast({
    title: '新密码已发送到您的邮箱',
    icon: 'success'
  })
  setTimeout(() => {
    uni.navigateBack()
  }, 1500)
  loading.value = false
}

// 模拟邮箱不存在
const simulateEmailNotFound = () => {
  uni.showModal({
    title: '提示',
    content: '该邮箱未注册',
    showCancel: false,
    success: () => {
      uni.navigateBack()
    }
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