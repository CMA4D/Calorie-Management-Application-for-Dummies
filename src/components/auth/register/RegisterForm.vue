<template>
  <view class="register-form">
    <form @submit="handleSubmit">
      <!-- 用户名输入框 -->
      <view class="form-item">
        <input
          type="text"
          v-model="formData.username"
          placeholder="请输入用户名"
          :disabled="loading"
        />
      </view>
      
      <!-- 邮箱输入框 -->
      <view class="form-item">
        <input
          type="email"
          v-model="formData.email"
          placeholder="请输入邮箱"
          :disabled="loading"
        />
      </view>
      
      <!-- 密码输入框 -->
      <view class="form-item">
        <input
          type="password"
          v-model="formData.password"
          placeholder="请输入密码"
          :disabled="loading"
        />
      </view>
      
      <!-- 确认密码输入框 -->
      <view class="form-item">
        <input
          type="password"
          v-model="formData.confirmPassword"
          placeholder="请确认密码"
          :disabled="loading"
        />
      </view>
      
      <!-- 注册按钮 -->
      <button
        class="submit-btn"
        :disabled="loading"
        :loading="loading"
        form-type="submit"
      >
        {{ loading ? '注册中...' : '注册' }}
      </button>
    </form>
  </view>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'

defineOptions({
  name: 'RegisterForm'
})

// 定义组件属性
const props = defineProps<{
  loading?: boolean
}>()

// 定义组件事件
const emit = defineEmits<{
  (e: 'submit', data: { username: string; password: string; confirmPassword: string; email: string }): void
}>()

// 表单数据
const formData = reactive({
  username: '',
  email: '',
  password: '',
  confirmPassword: ''
})

// 处理表单提交
const handleSubmit = () => {
  // 表单验证
  if (!formData.username) {
    uni.showToast({
      title: '请输入用户名',
      icon: 'none'
    })
    return
  }
  
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
  
  if (!formData.password) {
    uni.showToast({
      title: '请输入密码',
      icon: 'none'
    })
    return
  }
  
  if (!formData.confirmPassword) {
    uni.showToast({
      title: '请确认密码',
      icon: 'none'
    })
    return
  }
  
  if (formData.password !== formData.confirmPassword) {
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
.register-form {
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