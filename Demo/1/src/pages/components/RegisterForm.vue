<template>
  <view class="register-form">
    <!-- 用户名输入框 -->
    <view class="form-item">
      <text class="label">用户名</text>
      <input 
        type="text"
        v-model="formData.username"
        placeholder="请输入用户名"
        :disabled="loading"
      />
    </view>
    
    <!-- 密码输入框 -->
    <view class="form-item">
      <text class="label">密码</text>
      <input 
        type="password"
        v-model="formData.password"
        placeholder="请输入密码"
        :disabled="loading"
      />
    </view>
    
    <!-- 确认密码输入框 -->
    <view class="form-item">
      <text class="label">确认密码</text>
      <input 
        type="password"
        v-model="formData.confirmPassword"
        placeholder="请再次输入密码"
        :disabled="loading"
      />
    </view>
    
    <!-- 邮箱输入框 -->
    <view class="form-item">
      <text class="label">邮箱</text>
      <input 
        type="text"
        v-model="formData.email"
        placeholder="请输入邮箱"
        :disabled="loading"
      />
    </view>
    
    <!-- 注册按钮 -->
    <button 
      class="register-button"
      :loading="loading"
      :disabled="!isFormValid"
      @click="handleSubmit"
    >
      注册
    </button>
    
    <!-- 登录链接 -->
    <view class="login-link">
      <text>已有账号？</text>
      <text class="link" @click="handleLogin">立即登录</text>
    </view>
  </view>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

// 定义组件名称
defineOptions({
  name: 'registerForm'
})

// 定义组件属性
interface Props {
  loading?: boolean
}

// 定义组件事件
interface Emits {
  (e: 'submit', data: { 
    username: string
    password: string
    confirmPassword: string
    email: string
  }): void
}

const props = withDefaults(defineProps<Props>(), {
  loading: false
})

const emit = defineEmits<Emits>()

// 表单数据
const formData = ref({
  username: '',
  password: '',
  confirmPassword: '',
  email: ''
})

// 表单验证
const isFormValid = computed(() => {
  const { username, password, confirmPassword, email } = formData.value
  
  // 用户名不能为空
  if (username.trim() === '') return false
  
  // 密码不能为空且长度至少6位
  if (password.trim() === '' || password.length < 6) return false
  
  // 确认密码必须与密码一致
  if (password !== confirmPassword) return false
  
  // 邮箱格式验证
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  if (!emailRegex.test(email)) return false
  
  return true
})

// 处理表单提交
const handleSubmit = () => {
  if (!isFormValid.value) return
  
  emit('submit', {
    username: formData.value.username.trim(),
    password: formData.value.password,
    confirmPassword: formData.value.confirmPassword,
    email: formData.value.email.trim()
  })
}

// 处理登录点击
const handleLogin = () => {
  uni.navigateBack()
}
</script>

<style lang="scss">
/* 注册表单样式 */
.register-form {
  background-color: #fff;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
  
  /* 表单项样式 */
  .form-item {
    margin-bottom: 20px;
    
    /* 标签样式 */
    .label {
      font-size: 14px;
      color: #333;
      margin-bottom: 8px;
      display: block;
    }
    
    /* 输入框样式 */
    input {
      width: 100%;
      height: 44px;
      border: 1px solid #ddd;
      border-radius: 4px;
      padding: 0 12px;
      font-size: 14px;
      
      &:focus {
        border-color: #007AFF;
      }
      
      &:disabled {
        background-color: #f5f5f5;
      }
    }
  }
  
  /* 注册按钮样式 */
  .register-button {
    width: 100%;
    height: 44px;
    background-color: #007AFF;
    color: #fff;
    border-radius: 4px;
    font-size: 16px;
    margin-top: 30px;
    
    &:disabled {
      background-color: #ccc;
    }
  }
  
  /* 登录链接样式 */
  .login-link {
    text-align: center;
    margin-top: 20px;
    font-size: 14px;
    color: #666;
    
    .link {
      color: #007AFF;
      margin-left: 4px;
    }
  }
}
</style> 