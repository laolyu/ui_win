# python+lackey实现Windows系统,应用UI自动化测试
## 需求来源: 
  - PC业务线产品采用被动dll方式加载弹窗广告, 容易被杀毒软件报毒, 从而影响公司收入,
  - 因此需要实时的监测到报毒情况.因为软件报毒, 第三方杀软,360安全卫士,360杀毒,金山毒霸,腾讯电脑管家,是不会通知单你的,直接给予封杀.
  - 而获知到被报毒后,需要对应产品的负责人根据不同情况采取措施:
  - 比如360安全卫士,360杀毒环境>> 可以原封不动的换包去再次申请过白,过白通过后再上架, 过白前相应的报毒版本予以下架,更换为其他不报毒的安装包(要求平时有储备)
  -  金山毒霸环境>>一般是不予处理的, 去沟通也无果, 换包打包后会给继续报毒, 要求开发采取新的对抗措施应对
  - 腾讯管家环境>>出现报毒后可以通过邮件等沟通方式, 予以黑转白,但杀软自身有bug容易反复误报病毒.
## 测试目标: 实现对PC业务线产品的安全(报毒)测试,及时对报毒软件预警
## 测试方案:python+lackey实现pc端exe自动化
  1. vaware准备后各自杀软的测试环境, 需要精细化配置,部分无视也无法处理的报毒提示设置为不提示,以减轻代码的无效工作压力
  2. 把杀软各种报毒的经典场景截图, 需要点击的事件最好采用相对坐标的方式点击
  3. 封装lackey的各种事件的方法, 把需要测试的版本单独配置
  4. 采用多线程处理, 一个线程执行cmd安装操作, 一个线程处理UI事件