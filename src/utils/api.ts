export interface AnalysisResponse {
    success: boolean;
    foodName: string;
    calories: number;
  }
  
  // 上传图片并识别
  export const uploadImage = async (imageBase64: string, weight: number): Promise<any> => {   //后续应将any改为自定的AnalysisResponse接口
    const res = await uni.request({
      url: 'https://your-server-domain.com/api/receive', // 替换为实际服务器地址
      method: 'POST',
      data: {
        image: imageBase64,
        weight,
      },
    });
  
    if (res.statusCode === 200) {
      // return res.data;
      console.log('',res)
    } else {
      throw new Error('上传失败');
    }
  };