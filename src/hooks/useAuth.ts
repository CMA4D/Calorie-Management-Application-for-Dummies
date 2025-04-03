import { ref } from 'vue';

export default function useAuth() {
  // 登录逻辑
  const login = async (username: string, password: string): Promise<boolean> => {
    // 调用登录API（示例）
    if (username === 'admin' && password === '123456') {
      uni.setStorageSync('user', username);
      return true;
    }
    return false;
  };

  return {
    login,
  };
}