<template>
  <view class="login-form">
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
    
    <!-- 登录按钮 -->
    <button 
      class="login-button"
      :loading="loading"
      :disabled="!isFormValid"
      @click="handleSubmit"
    >
      登录
    </button>
    
    <!-- 注册链接 -->
    <view class="register-link">
      <text>还没有账号？</text>
      <text class="link" @click="handleRegister">立即注册</text>
    </view>
  </view>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

// 定义组件名称
defineOptions({
  name: 'loginForm'
})

// 定义组件属性
interface Props {
  loading?: boolean
}

// 定义组件事件
interface Emits {
  (e: 'submit', data: { username: string; password: string }): void
}

const props = withDefaults(defineProps<Props>(), {
  loading: false
})

const emit = defineEmits<Emits>()

// 表单数据
const formData = ref({
  username: '',
  password: ''
})

// 表单验证
const isFormValid = computed(() => {
  return formData.value.username.trim() !== '' && 
         formData.value.password.trim() !== ''
})

// 处理表单提交
const handleSubmit = () => {
  if (!isFormValid.value) return
  
  emit('submit', {
    username: formData.value.username.trim(),
    password: formData.value.password.trim()
  })
}

// 处理注册点击
const handleRegister = () => {
  uni.navigateTo({
    url: '/pages/Register'
  })
}
</script>

<style lang="scss">
/* 登录表单样式 */
.login-form {
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
  
  /* 登录按钮样式 */
  .login-button {
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
  
  /* 注册链接样式 */
  .register-link {
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