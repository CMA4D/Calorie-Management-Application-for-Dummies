import { uploadImage } from '@/utils/api';

export default function useFoodAnalysis() {
  // 分析食物
  const analyzeFood = async (imageBase64: string, weight: number) => {
    try {
      const response = await uploadImage(imageBase64, weight);
      if (response.success) {
        return response;
      }
    } catch (error) {
      console.error(error);
    }
    return null;
  };

  return {
    analyzeFood,
  };
}