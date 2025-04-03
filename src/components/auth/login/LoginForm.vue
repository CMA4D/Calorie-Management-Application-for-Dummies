<template>
  <view class="login-form">
    <!-- 用户名输入框 -->
    <view class="form-item">
      <input
        type="text"
        v-model="formData.username"
        placeholder="请输入用户名"
      />
    </view>
    
    <!-- 密码输入框 -->
    <view class="form-item">
      <input
        type="password"
        v-model="formData.password"
        placeholder="请输入密码"
      />
    </view>
    
    <!-- 记住密码选项 -->
    <view class="remember-password">
      <checkbox-group @change="handleRememberChange">
        <label>
          <checkbox :checked="rememberPassword" />
          <text>记住密码</text>
        </label>
      </checkbox-group>
      <text class="forget-password" @click="goToResetPassword">忘记密码？</text>
    </view>
    
    <!-- 登录按钮 -->
    <button 
      class="login-button"
      :disabled="loading"
      @click="handleSubmit"
    >
      {{ loading ? '登录中...' : '登录' }}
    </button>
    
    <!-- 注册链接 -->
    <view class="register-link">
      <text>还没有账号？</text>
      <text @click="goToRegister">立即注册</text>
    </view>
  </view>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useUserStore } from '@/stores/modules/user'

const props = defineProps<{
  loading: boolean
}>()

const emit = defineEmits<{
  (e: 'submit', data: { username: string; password: string; remember: boolean }): void
}>()

// 表单数据
const formData = ref({
  username: '',
  password: '',
  remember: false
})

// 表单引用
const formRef = ref<any>(null)

// 记住密码状态
const rememberPassword = ref(false)

// 用户状态管理
const userStore = useUserStore()

// 处理记住密码变化
const handleRememberChange = (e: any) => {
  rememberPassword.value = e.detail.value.length > 0
  formData.value.remember = rememberPassword.value
}

// 设置记住的账号密码
const setRememberedCredentials = (username: string, password: string) => {
  formData.value.username = username
  formData.value.password = password
  formData.value.remember = true
  rememberPassword.value = true
}

// 暴露方法给父组件
defineExpose({
  setRememberedCredentials
})

// 处理表单提交
const handleSubmit = () => {
  if (!formData.value.username || !formData.value.password) {
    uni.showToast({
      title: '请输入用户名和密码',
      icon: 'none'
    })
    return
  }
  
  emit('submit', {
    username: formData.value.username,
    password: formData.value.password,
    remember: rememberPassword.value
  })
}

// 跳转到注册页面
const goToRegister = () => {
  uni.navigateTo({
    url: '/pages/auth/Register'
  })
}

// 跳转到重置密码页面
const goToResetPassword = () => {
  uni.navigateTo({
    url: '/pages/auth/ResetPassword'
  })
}

// 页面加载时检查是否有保存的用户名
onMounted(() => {
  const rememberedUsername = uni.getStorageSync('rememberedUsername')
  const rememberedPassword = uni.getStorageSync('rememberedPassword')
  
  if (rememberedUsername && rememberedPassword) {
    setRememberedCredentials(rememberedUsername, rememberedPassword)
  }
})
</script>

<style lang="scss">
.login-form {
  background-color: #fff;
  border-radius: 12px;
  padding: 20px;
  margin-top: 20px;
  
  /* 表单项样式 */
  .form-item {
    margin-bottom: 20px;
    
    input {
      width: 100%;
      height: 48px;
      border: 1px solid #ddd;
      border-radius: 8px;
      padding: 0 15px;
      font-size: 16px;
      
      &:focus {
        border-color: #007AFF;
      }
    }
  }
  
  /* 记住密码样式 */
  .remember-password {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    
    checkbox-group {
      display: flex;
      align-items: center;
      
      label {
        display: flex;
        align-items: center;
        font-size: 14px;
        color: #666;
        
        checkbox {
          margin-right: 5px;
        }
      }
    }
    
    .forget-password {
      font-size: 14px;
      color: #007AFF;
    }
  }
  
  /* 登录按钮样式 */
  .login-button {
    width: 100%;
    height: 48px;
    background-color: #007AFF;
    color: #fff;
    border-radius: 8px;
    font-size: 16px;
    margin-bottom: 20px;
    
    &:disabled {
      background-color: #ccc;
    }
  }
  
  /* 注册链接样式 */
  .register-link {
    text-align: center;
    font-size: 14px;
    color: #666;
    
    text:last-child {
      color: #007AFF;
      margin-left: 5px;
    }
  }
}
</style> 