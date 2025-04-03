<template>
  <view class="reset-password-form">
    <form @submit="handleSubmit">
      <!-- 邮箱输入框 -->
      <view class="form-item">
        <input
          type="email"
          v-model="formData.email"
          placeholder="请输入邮箱"
          :disabled="loading"
        />
      </view>
      
      <!-- 验证码输入框 -->
      <view class="form-item code-item">
        <input
          type="text"
          v-model="formData.code"
          placeholder="请输入验证码"
          :disabled="loading"
        />
        <button
          class="code-btn"
          :disabled="loading || countdown > 0"
          @click="handleSendCode"
        >
          {{ countdown > 0 ? `${countdown}s后重试` : '获取验证码' }}
        </button>
      </view>
      
      <!-- 新密码输入框 -->
      <view class="form-item">
        <input
          type="password"
          v-model="formData.newPassword"
          placeholder="请输入新密码"
          :disabled="loading"
        />
      </view>
      
      <!-- 确认密码输入框 -->
      <view class="form-item">
        <input
          type="password"
          v-model="formData.confirmPassword"
          placeholder="请确认新密码"
          :disabled="loading"
        />
      </view>
      
      <!-- 提交按钮 -->
      <button
        class="submit-btn"
        :disabled="loading"
        :loading="loading"
        form-type="submit"
      >
        {{ loading ? '提交中...' : '重置密码' }}
      </button>
    </form>
  </view>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'

defineOptions({
  name: 'ResetPasswordForm'
})

// 定义组件属性
const props = defineProps<{
  loading?: boolean
}>()

// 定义组件事件
const emit = defineEmits<{
  (e: 'submit', data: { email: string; code: string; newPassword: string; confirmPassword: string }): void
  (e: 'sendCode', email: string): void
}>()

// 表单数据
const formData = reactive({
  email: '',
  code: '',
  newPassword: '',
  confirmPassword: ''
})

// 倒计时
const countdown = ref(0)

// 处理发送验证码
const handleSendCode = () => {
  if (!formData.email) {
    uni.showToast({
      title: '请输入邮箱',
      icon: 'none'
    })
    return
  }
  
  // 邮箱格式验证
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  if (!emailRegex.test(formData.email)) {
    uni.showToast({
      title: '请输入正确的邮箱格式',
      icon: 'none'
    })
    return
  }
  
  // 触发发送验证码事件
  emit('sendCode', formData.email)
  
  // 开始倒计时
  countdown.value = 60
  const timer = setInterval(() => {
    countdown.value--
    if (countdown.value <= 0) {
      clearInterval(timer)
    }
  }, 1000)
}

// 处理表单提交
const handleSubmit = () => {
  // 表单验证
  if (!formData.email) {
    uni.showToast({
      title: '请输入邮箱',
      icon: 'none'
    })
    return
  }
  
  // 邮箱格式验证
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  if (!emailRegex.test(formData.email)) {
    uni.showToast({
      title: '请输入正确的邮箱格式',
      icon: 'none'
    })
    return
  }
  
  if (!formData.code) {
    uni.showToast({
      title: '请输入验证码',
      icon: 'none'
    })
    return
  }
  
  if (!formData.newPassword) {
    uni.showToast({
      title: '请输入新密码',
      icon: 'none'
    })
    return
  }
  
  if (!formData.confirmPassword) {
    uni.showToast({
      title: '请确认新密码',
      icon: 'none'
    })
    return
  }
  
  if (formData.newPassword !== formData.confirmPassword) {
    uni.showToast({
      title: '两次输入的密码不一致',
      icon: 'none'
    })
    return
  }
  
  // 触发提交事件
  emit('submit', { ...formData })
}
</script>

<style lang="scss">
.reset-password-form {
  background-color: #fff;
  border-radius: 8px;
  padding: 20px;
  margin-top: 20px;
  
  .form-item {
    margin-bottom: 20px;
    
    input {
      width: 100%;
      height: 44px;
      border: 1px solid #ddd;
      border-radius: 4px;
      padding: 0 15px;
      font-size: 16px;
      
      &:focus {
        border-color: #007AFF;
      }
      
      &[disabled] {
        background-color: #f5f5f5;
        color: #999;
      }
    }
  }
  
  .code-item {
    display: flex;
    gap: 10px;
    
    input {
      flex: 1;
    }
    
    .code-btn {
      width: 120px;
      height: 44px;
      background-color: #007AFF;
      color: #fff;
      border-radius: 4px;
      font-size: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      
      &[disabled] {
        background-color: #ccc;
      }
    }
  }
  
  .submit-btn {
    width: 100%;
    height: 44px;
    background-color: #007AFF;
    color: #fff;
    border-radius: 4px;
    font-size: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    
    &[disabled] {
      background-color: #ccc;
    }
  }
}
</style> 