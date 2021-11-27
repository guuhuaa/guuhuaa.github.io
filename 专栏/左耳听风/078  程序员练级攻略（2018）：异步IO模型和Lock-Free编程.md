<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>078  程序员练级攻略（2018）：异步IO模型和Lock-Free编程.md</title>
        <!-- Spectre.css framework -->
        <link rel="stylesheet" href="../../static/index.css">
        <!-- theme css & js -->
        <meta name="generator" content="Hexo 4.2.0">
    </head>

<body>

<div class="book-container">
    <div class="book-sidebar">
        <div class="book-brand">
            <a href="../../index.html">
                <img src="../../static/favicon.png">
                <span>技术文章摘抄</span>
            </a>
        </div>
        <div class="book-menu uncollapsible">
            <ul class="uncollapsible">
                <li><a href="../../index.html" class="current-tab">首页</a></li>
            </ul>

            <ul class="uncollapsible">
                <li><a href="../index.html">上一级</a></li>
            </ul>

            <ul class="uncollapsible">
                <li>

                    
                    <a href="000&#32;开篇词&#32;&#32;洞悉技术的本质，享受科技的乐趣.md">000 开篇词  洞悉技术的本质，享受科技的乐趣.md</a>

                </li>
                <li>

                    
                    <a href="001&#32;&#32;程序员如何用技术变现（上）.md">001  程序员如何用技术变现（上）.md</a>

                </li>
                <li>

                    
                    <a href="002&#32;&#32;程序员如何用技术变现（下）.md">002  程序员如何用技术变现（下）.md</a>

                </li>
                <li>

                    
                    <a href="003&#32;&#32;Equifax信息泄露始末.md">003  Equifax信息泄露始末.md</a>

                </li>
                <li>

                    
                    <a href="004&#32;&#32;从Equifax信息泄露看数据安全.md">004  从Equifax信息泄露看数据安全.md</a>

                </li>
                <li>

                    
                    <a href="005&#32;&#32;何为技术领导力.md">005  何为技术领导力.md</a>

                </li>
                <li>

                    
                    <a href="006&#32;&#32;如何拥有技术领导力.md">006  如何拥有技术领导力.md</a>

                </li>
                <li>

                    
                    <a href="007&#32;&#32;推荐阅读：每个程序员都该知道的事.md">007  推荐阅读：每个程序员都该知道的事.md</a>

                </li>
                <li>

                    
                    <a href="008&#32;&#32;Go语言，Docker和新技术.md">008  Go语言，Docker和新技术.md</a>

                </li>
                <li>

                    
                    <a href="009&#32;&#32;答疑解惑：渴望、热情和选择.md">009  答疑解惑：渴望、热情和选择.md</a>

                </li>
                <li>

                    
                    <a href="010&#32;&#32;如何成为一个大家愿意追随的Leader？.md">010  如何成为一个大家愿意追随的Leader？.md</a>

                </li>
                <li>

                    
                    <a href="011&#32;&#32;程序中的错误处理：错误返回码和异常捕捉.md">011  程序中的错误处理：错误返回码和异常捕捉.md</a>

                </li>
                <li>

                    
                    <a href="012&#32;&#32;程序中的错误处理：异步编程和最佳实践.md">012  程序中的错误处理：异步编程和最佳实践.md</a>

                </li>
                <li>

                    
                    <a href="013&#32;&#32;魔数&#32;0x5f3759df.md">013  魔数 0x5f3759df.md</a>

                </li>
                <li>

                    
                    <a href="014&#32;&#32;推荐阅读：机器学习101.md">014  推荐阅读：机器学习101.md</a>

                </li>
                <li>

                    
                    <a href="015&#32;&#32;时间管理：同扭曲时间的事儿抗争.md">015  时间管理：同扭曲时间的事儿抗争.md</a>

                </li>
                <li>

                    
                    <a href="016&#32;&#32;时间管理：投资赚取时间.md">016  时间管理：投资赚取时间.md</a>

                </li>
                <li>

                    
                    <a href="017&#32;&#32;故障处理最佳实践：应对故障.md">017  故障处理最佳实践：应对故障.md</a>

                </li>
                <li>

                    
                    <a href="018&#32;&#32;故障处理最佳实践：故障改进.md">018  故障处理最佳实践：故障改进.md</a>

                </li>
                <li>

                    
                    <a href="019&#32;&#32;答疑解惑：我们应该能够识别的表象和本质.md">019  答疑解惑：我们应该能够识别的表象和本质.md</a>

                </li>
                <li>

                    
                    <a href="020&#32;&#32;分布式系统架构的冰与火.md">020  分布式系统架构的冰与火.md</a>

                </li>
                <li>

                    
                    <a href="021&#32;&#32;从亚马逊的实践，谈分布式系统的难点.md">021  从亚马逊的实践，谈分布式系统的难点.md</a>

                </li>
                <li>

                    
                    <a href="022&#32;&#32;分布式系统的技术栈.md">022  分布式系统的技术栈.md</a>

                </li>
                <li>

                    
                    <a href="023&#32;&#32;分布式系统关键技术：全栈监控.md">023  分布式系统关键技术：全栈监控.md</a>

                </li>
                <li>

                    
                    <a href="024&#32;&#32;分布式系统关键技术：服务调度.md">024  分布式系统关键技术：服务调度.md</a>

                </li>
                <li>

                    
                    <a href="025&#32;&#32;分布式系统关键技术：流量与数据调度.md">025  分布式系统关键技术：流量与数据调度.md</a>

                </li>
                <li>

                    
                    <a href="026&#32;&#32;洞悉PaaS平台的本质.md">026  洞悉PaaS平台的本质.md</a>

                </li>
                <li>

                    
                    <a href="027&#32;&#32;推荐阅读：分布式系统架构经典资料.md">027  推荐阅读：分布式系统架构经典资料.md</a>

                </li>
                <li>

                    
                    <a href="028&#32;&#32;编程范式游记（1）-&#32;起源.md">028  编程范式游记（1）- 起源.md</a>

                </li>
                <li>

                    
                    <a href="029&#32;&#32;编程范式游记（2）-&#32;泛型编程.md">029  编程范式游记（2）- 泛型编程.md</a>

                </li>
                <li>

                    
                    <a href="030&#32;&#32;编程范式游记（3）&#32;-&#32;类型系统和泛型的本质.md">030  编程范式游记（3） - 类型系统和泛型的本质.md</a>

                </li>
                <li>

                    
                    <a href="031&#32;&#32;Git协同工作流，你该怎样选.md">031  Git协同工作流，你该怎样选.md</a>

                </li>
                <li>

                    
                    <a href="032&#32;&#32;推荐阅读：分布式数据调度相关论文.md">032  推荐阅读：分布式数据调度相关论文.md</a>

                </li>
                <li>

                    
                    <a href="033&#32;&#32;编程范式游记（4）-&#32;函数式编程.md">033  编程范式游记（4）- 函数式编程.md</a>

                </li>
                <li>

                    
                    <a href="034&#32;&#32;编程范式游记（5）-&#32;修饰器模式.md">034  编程范式游记（5）- 修饰器模式.md</a>

                </li>
                <li>

                    
                    <a href="035&#32;&#32;编程范式游记（6）-&#32;面向对象编程.md">035  编程范式游记（6）- 面向对象编程.md</a>

                </li>
                <li>

                    
                    <a href="036&#32;&#32;编程范式游记（7）-&#32;基于原型的编程范式.md">036  编程范式游记（7）- 基于原型的编程范式.md</a>

                </li>
                <li>

                    
                    <a href="037&#32;&#32;编程范式游记（8）-&#32;Go&#32;语言的委托模式.md">037  编程范式游记（8）- Go 语言的委托模式.md</a>

                </li>
                <li>

                    
                    <a href="038&#32;&#32;编程范式游记（9）-&#32;编程的本质.md">038  编程范式游记（9）- 编程的本质.md</a>

                </li>
                <li>

                    
                    <a href="039&#32;&#32;编程范式游记（10）-&#32;逻辑编程范式.md">039  编程范式游记（10）- 逻辑编程范式.md</a>

                </li>
                <li>

                    
                    <a href="040&#32;&#32;编程范式游记（11）-&#32;程序世界里的编程范式.md">040  编程范式游记（11）- 程序世界里的编程范式.md</a>

                </li>
                <li>

                    
                    <a href="041&#32;&#32;弹力设计篇之“认识故障和弹力设计”.md">041  弹力设计篇之“认识故障和弹力设计”.md</a>

                </li>
                <li>

                    
                    <a href="042&#32;&#32;弹力设计篇之“隔离设计”.md">042  弹力设计篇之“隔离设计”.md</a>

                </li>
                <li>

                    
                    <a href="043&#32;&#32;弹力设计篇之“异步通讯设计”.md">043  弹力设计篇之“异步通讯设计”.md</a>

                </li>
                <li>

                    
                    <a href="044&#32;&#32;弹力设计篇之“幂等性设计”.md">044  弹力设计篇之“幂等性设计”.md</a>

                </li>
                <li>

                    
                    <a href="045&#32;&#32;弹力设计篇之“服务的状态”.md">045  弹力设计篇之“服务的状态”.md</a>

                </li>
                <li>

                    
                    <a href="046&#32;&#32;弹力设计篇之“补偿事务”.md">046  弹力设计篇之“补偿事务”.md</a>

                </li>
                <li>

                    
                    <a href="047&#32;&#32;弹力设计篇之“重试设计”.md">047  弹力设计篇之“重试设计”.md</a>

                </li>
                <li>

                    
                    <a href="048&#32;&#32;弹力设计篇之“熔断设计”.md">048  弹力设计篇之“熔断设计”.md</a>

                </li>
                <li>

                    
                    <a href="049&#32;&#32;弹力设计篇之“限流设计”.md">049  弹力设计篇之“限流设计”.md</a>

                </li>
                <li>

                    
                    <a href="050&#32;&#32;弹力设计篇之“降级设计”.md">050  弹力设计篇之“降级设计”.md</a>

                </li>
                <li>

                    
                    <a href="051&#32;&#32;弹力设计篇之“弹力设计总结”.md">051  弹力设计篇之“弹力设计总结”.md</a>

                </li>
                <li>

                    
                    <a href="052&#32;&#32;区块链技术&#32;-&#32;区块链的革命性及技术概要.md">052  区块链技术 - 区块链的革命性及技术概要.md</a>

                </li>
                <li>

                    
                    <a href="053&#32;&#32;区块链技术&#32;-&#32;区块链技术细节&#32;-&#32;哈希算法.md">053  区块链技术 - 区块链技术细节 - 哈希算法.md</a>

                </li>
                <li>

                    
                    <a href="054&#32;&#32;区块链技术&#32;-&#32;区块链技术细节&#32;-&#32;加密和挖矿.md">054  区块链技术 - 区块链技术细节 - 加密和挖矿.md</a>

                </li>
                <li>

                    
                    <a href="055&#32;&#32;区块链技术&#32;-&#32;去中心化的共识机制.md">055  区块链技术 - 去中心化的共识机制.md</a>

                </li>
                <li>

                    
                    <a href="056&#32;&#32;区块链技术&#32;-&#32;智能合约.md">056  区块链技术 - 智能合约.md</a>

                </li>
                <li>

                    
                    <a href="057&#32;&#32;区块链技术&#32;-&#32;传统金融和虚拟货币.md">057  区块链技术 - 传统金融和虚拟货币.md</a>

                </li>
                <li>

                    
                    <a href="058&#32;&#32;管理设计篇之分布式锁.md">058  管理设计篇之分布式锁.md</a>

                </li>
                <li>

                    
                    <a href="059&#32;&#32;管理设计篇之配置中心.md">059  管理设计篇之配置中心.md</a>

                </li>
                <li>

                    
                    <a href="060&#32;&#32;管理设计篇之边车模式.md">060  管理设计篇之边车模式.md</a>

                </li>
                <li>

                    
                    <a href="061&#32;&#32;管理设计篇之服务网格.md">061  管理设计篇之服务网格.md</a>

                </li>
                <li>

                    
                    <a href="062&#32;&#32;管理设计篇之网关模式.md">062  管理设计篇之网关模式.md</a>

                </li>
                <li>

                    
                    <a href="063&#32;&#32;管理设计篇之部署升级策略.md">063  管理设计篇之部署升级策略.md</a>

                </li>
                <li>

                    
                    <a href="064&#32;&#32;性能设计篇之缓存.md">064  性能设计篇之缓存.md</a>

                </li>
                <li>

                    
                    <a href="065&#32;&#32;性能设计篇之异步处理.md">065  性能设计篇之异步处理.md</a>

                </li>
                <li>

                    
                    <a href="066&#32;&#32;性能设计篇之数据库扩展.md">066  性能设计篇之数据库扩展.md</a>

                </li>
                <li>

                    
                    <a href="067&#32;&#32;性能设计篇之秒杀.md">067  性能设计篇之秒杀.md</a>

                </li>
                <li>

                    
                    <a href="068&#32;&#32;性能设计篇之边缘计算.md">068  性能设计篇之边缘计算.md</a>

                </li>
                <li>

                    
                    <a href="069&#32;&#32;程序员练级攻略（2018）：开篇词.md">069  程序员练级攻略（2018）：开篇词.md</a>

                </li>
                <li>

                    
                    <a href="070&#32;&#32;程序员练级攻略（2018）：零基础启蒙.md">070  程序员练级攻略（2018）：零基础启蒙.md</a>

                </li>
                <li>

                    
                    <a href="071&#32;&#32;程序员练级攻略（2018）：正式入门.md">071  程序员练级攻略（2018）：正式入门.md</a>

                </li>
                <li>

                    
                    <a href="072&#32;&#32;程序员练级攻略（2018）：程序员修养.md">072  程序员练级攻略（2018）：程序员修养.md</a>

                </li>
                <li>

                    
                    <a href="073&#32;&#32;程序员练级攻略（2018）：编程语言.md">073  程序员练级攻略（2018）：编程语言.md</a>

                </li>
                <li>

                    
                    <a href="074&#32;&#32;程序员练级攻略：理论学科.md">074  程序员练级攻略：理论学科.md</a>

                </li>
                <li>

                    
                    <a href="075&#32;&#32;程序员练级攻略（2018）：系统知识.md">075  程序员练级攻略（2018）：系统知识.md</a>

                </li>
                <li>

                    
                    <a href="076&#32;&#32;程序员练级攻略（2018）：软件设计.md">076  程序员练级攻略（2018）：软件设计.md</a>

                </li>
                <li>

                    
                    <a href="077&#32;&#32;程序员练级攻略（2018）：Linux系统、内存和网络.md">077  程序员练级攻略（2018）：Linux系统、内存和网络.md</a>

                </li>
                <li>

                    <a class="current-tab" href="078&#32;&#32;程序员练级攻略（2018）：异步IO模型和Lock-Free编程.md">078  程序员练级攻略（2018）：异步IO模型和Lock-Free编程.md</a>
                    

                </li>
                <li>

                    
                    <a href="079&#32;&#32;程序员练级攻略（2018）：Java底层知识.md">079  程序员练级攻略（2018）：Java底层知识.md</a>

                </li>
                <li>

                    
                    <a href="080&#32;&#32;程序员练级攻略（2018）：数据库.md">080  程序员练级攻略（2018）：数据库.md</a>

                </li>
                <li>

                    
                    <a href="081&#32;&#32;程序员练级攻略（2018）：分布式架构入门.md">081  程序员练级攻略（2018）：分布式架构入门.md</a>

                </li>
                <li>

                    
                    <a href="082&#32;&#32;程序员练级攻略（2018）：分布式架构经典图书和论文.md">082  程序员练级攻略（2018）：分布式架构经典图书和论文.md</a>

                </li>
                <li>

                    
                    <a href="083&#32;&#32;程序员练级攻略（2018）：分布式架构工程设计.md">083  程序员练级攻略（2018）：分布式架构工程设计.md</a>

                </li>
                <li>

                    
                    <a href="084&#32;&#32;程序员练级攻略（2018）：微服务.md">084  程序员练级攻略（2018）：微服务.md</a>

                </li>
                <li>

                    
                    <a href="085&#32;&#32;程序员练级攻略（2018）：容器化和自动化运维.md">085  程序员练级攻略（2018）：容器化和自动化运维.md</a>

                </li>
                <li>

                    
                    <a href="086&#32;&#32;程序员练级攻略（2018）：机器学习和人工智能.md">086  程序员练级攻略（2018）：机器学习和人工智能.md</a>

                </li>
                <li>

                    
                    <a href="087&#32;&#32;程序员练级攻略（2018）：前端基础和底层原理.md">087  程序员练级攻略（2018）：前端基础和底层原理.md</a>

                </li>
                <li>

                    
                    <a href="088&#32;&#32;程序员练级攻略（2018）：前端性能优化和框架.md">088  程序员练级攻略（2018）：前端性能优化和框架.md</a>

                </li>
                <li>

                    
                    <a href="089&#32;&#32;程序员练级攻略（2018）：UIUX设计.md">089  程序员练级攻略（2018）：UIUX设计.md</a>

                </li>
                <li>

                    
                    <a href="090&#32;&#32;程序员练级攻略（2018）：技术资源集散地.md">090  程序员练级攻略（2018）：技术资源集散地.md</a>

                </li>
                <li>

                    
                    <a href="091&#32;&#32;程序员面试攻略：面试前的准备.md">091  程序员面试攻略：面试前的准备.md</a>

                </li>
                <li>

                    
                    <a href="092&#32;&#32;程序员面试攻略：面试中的技巧.md">092  程序员面试攻略：面试中的技巧.md</a>

                </li>
                <li>

                    
                    <a href="093&#32;&#32;程序员面试攻略：面试风格.md">093  程序员面试攻略：面试风格.md</a>

                </li>
                <li>

                    
                    <a href="094&#32;&#32;程序员面试攻略：实力才是王中王.md">094  程序员面试攻略：实力才是王中王.md</a>

                </li>
                <li>

                    
                    <a href="095&#32;&#32;高效学习：端正学习态度.md">095  高效学习：端正学习态度.md</a>

                </li>
                <li>

                    
                    <a href="096&#32;&#32;高效学习：源头、原理和知识地图.md">096  高效学习：源头、原理和知识地图.md</a>

                </li>
                <li>

                    
                    <a href="097&#32;&#32;高效学习：深度，归纳和坚持实践.md">097  高效学习：深度，归纳和坚持实践.md</a>

                </li>
                <li>

                    
                    <a href="098&#32;&#32;高效学习：如何学习和阅读代码.md">098  高效学习：如何学习和阅读代码.md</a>

                </li>
                <li>

                    
                    <a href="099&#32;&#32;高效学习：面对枯燥和量大的知识.md">099  高效学习：面对枯燥和量大的知识.md</a>

                </li>
                <li>

                    
                    <a href="100&#32;&#32;高效沟通：Talk和Code同等重要.md">100  高效沟通：Talk和Code同等重要.md</a>

                </li>
                <li>

                    
                    <a href="101&#32;&#32;高效沟通：沟通阻碍和应对方法.md">101  高效沟通：沟通阻碍和应对方法.md</a>

                </li>
                <li>

                    
                    <a href="102&#32;&#32;高效沟通：沟通方式及技巧.md">102  高效沟通：沟通方式及技巧.md</a>

                </li>
                <li>

                    
                    <a href="103&#32;&#32;高效沟通：沟通技术.md">103  高效沟通：沟通技术.md</a>

                </li>
                <li>

                    
                    <a href="104&#32;&#32;高效沟通：好老板要善于提问.md">104  高效沟通：好老板要善于提问.md</a>

                </li>
                <li>

                    
                    <a href="105&#32;&#32;高效沟通：好好说话的艺术.md">105  高效沟通：好好说话的艺术.md</a>

                </li>
                <li>

                    
                    <a href="106&#32;加餐&#32;&#32;谈谈我的“三观”.md">106 加餐  谈谈我的“三观”.md</a>

                </li>
                <li>

                    
                    <a href="107&#32;结束语&#32;&#32;业精于勤，行成于思.md">107 结束语  业精于勤，行成于思.md</a>

                </li>
            </ul>

        </div>
    </div>

    <div class="sidebar-toggle" onclick="sidebar_toggle()" onmouseover="add_inner()" onmouseleave="remove_inner()">
        <div class="sidebar-toggle-inner"></div>
    </div>

    <script>
        function add_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.add('show')
        }

        function remove_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.remove('show')
        }

        function sidebar_toggle() {
            let sidebar_toggle = document.querySelector('.sidebar-toggle')
            let sidebar = document.querySelector('.book-sidebar')
            let content = document.querySelector('.off-canvas-content')
            if (sidebar_toggle.classList.contains('extend')) { // show
                sidebar_toggle.classList.remove('extend')
                sidebar.classList.remove('hide')
                content.classList.remove('extend')
            } else { // hide
                sidebar_toggle.classList.add('extend')
                sidebar.classList.add('hide')
                content.classList.add('extend')
            }
        }
    </script>

    <div class="off-canvas-content">
        <div class="columns">
            <div class="column col-12 col-lg-12">
                <div class="book-navbar">
                    <!-- For Responsive Layout -->
                    <header class="navbar">
                        <section class="navbar-section">
                            <a onclick="open_sidebar()">
                                <i class="icon icon-menu"></i>
                            </a>
                        </section>
                    </header>
                </div>
                <div class="book-content" style="max-width: 960px; margin: 0 auto;
    overflow-x: auto;
    overflow-y: hidden;">
                    <div class="book-post">
                        <p id="tip" align="center"></p>
                        <div><h1>078  程序员练级攻略（2018）：异步IO模型和Lock-Free编程</h1>
<h1>异步 I/O 模型</h1>
<p>异步 I/O 模型是我个人觉得所有程序员都必需要学习的一门技术或是编程方法，这其中的设计模式或是解决方法可以借鉴到分布式架构上来。再说一遍，学习这些模型，是非常非常重要的，你千万要认真学习。</p>
<p>史蒂文斯（Stevens）在《<a href="https://book.douban.com/subject/4859464/">UNIX 网络编程</a>》一书 6.2 I/O Models 中介绍了五种 I/O 模型。</p>
<ul>
<li>阻塞 I/O</li>
<li>非阻塞 I/O</li>
<li>I/O 的多路复用（select 和 poll）</li>
<li>信号驱动的 I/O（SIGIO）</li>
<li>异步 I/O（POSIX 的 aio_functions）</li>
</ul>
<p>然后，在前面我们也阅读过了 - <a href="https://en.wikipedia.org/wiki/C10k_problem">C10K Problem</a> 。相信你对 I/O 模型也有了一定的了解。 这里，我们需要更为深入地学习 I/O 模型，尤其是其中的异步 I/O 模型。</p>
<p>首先，我们看一篇和 Java 相关的 I/O 模型的文章来复习一下之前的内容。<a href="https://www.slideshare.net/e456/tyma-paulmultithreaded1">Thousands of Threads and Blocking I/O: The Old Way to Write Java Servers Is New Again (and Way Better)</a> ，这个 PPT 中不仅回顾和比较了各种 I/O 模型，而且还有各种比较细节的方案和说明，是一篇非常不错的文章。</p>
<p>然后，你可以看一篇 Java 相关的 PPT - 道格·莱亚（Doug Lea）的 <a href="http://gee.cs.oswego.edu/dl/cpjslides/nio.pdf">Scalable IO in Java</a>，这样你会对一些概念有个了解。</p>
<p>接下来，我们需要了解一下各种异步 I/O 的实现和设计方式。</p>
<ul>
<li><a href="https://www.ibm.com/developerworks/library/l-async/">IBM - Boost application performance using asynchronous I/O</a> ，这是一篇关于 AIO 的文章。</li>
<li><a href="https://www.usenix.org/legacy/event/usenix04/tech/general/full_papers/elmeleegy/elmeleegy_html/html.html">Lazy Asynchronous I/O For Event-Driven Servers</a> ，这篇文章也很不错。</li>
<li>另外，异步 I/O 模型中的 <a href="https://docs.microsoft.com/en-us/windows/desktop/FileIO/i-o-completion-ports">Windows I/O Completion Ports</a> , 你也需要了解一下。如果 MSDN 上的这个手册不容易读，你可以看看这篇文章 <a href="http://sysinternals.d4rk4.ru/Information/IoCompletionPorts.html">Inside I/O Completion Ports</a>。另外，关于 Windows，<a href="https://book.douban.com/subject/6935552/">Windows Internals</a> 这本书你可以仔细读一下，非常不错的。其中有一节 I/O Processing 也是很不错的，这里我给一个网上免费的链接<a href="https://flylib.com/books/en/4.491.1.85/1/">I/O Processing</a> 你可以看看 Windows 是怎么玩的。</li>
<li>接下来是 Libevent。你可以看一下其主要维护人员尼克·马修森（Nick Mathewson）写的 <a href="http://www.wangafu.net/~nickm/libevent-book/">libevent 2.0 book</a>。还有一本国人写的电子书 《<a href="https://aceld.gitbooks.io/libevent/content/">Libevent 深入浅出</a>》。</li>
<li>再接下来是 Libuv。你可以看一下其官网的 <a href="http://docs.libuv.org/en/v1.x/design.html">Libuv Design Overview</a> 了解一下。</li>
</ul>
<p>我简单总结一下，基本上来说，异步 I/O 模型的发展技术是： select -&gt; poll -&gt; epoll -&gt; aio -&gt; libevent -&gt; libuv。Unix/Linux 用了好几十年走过这些技术的变迁，然而，都不如 Windows I/O Completion Port 设计得好（免责声明：这个观点纯属个人观点。相信你仔细研究这些 I/O 模型后，你会得到你自己的判断）。</p>
<p>看过这些各种异步 I/O 模式的实现以后，相信你会看到一个编程模式——Reactor 模式。下面是这个模式的相关文章（读这三篇就够了）。</p>
<ul>
<li><a href="https://dzone.com/articles/understanding-reactor-pattern-thread-based-and-eve">Understanding Reactor Pattern: Thread-Based and Event-Driven</a></li>
<li><a href="http://www.cs.wustl.edu/~schmidt/PDF/reactor-siemens.pdf">Reactor Pattern</a></li>
<li><a href="https://www.celum.com/en/blog/technology/the-reactor-pattern-and-non-blocking-io">The reactor pattern and non-blocking IO</a></li>
</ul>
<p>然后是几篇有意思的延伸阅读文章。</p>
<ul>
<li><a href="http://highscalability.com/blog/2013/5/13/the-secret-to-10-million-concurrent-connections-the-kernel-i.html">The Secret To 10 Million Concurrent Connections -The Kernel Is The Problem, Not The Solution</a> - C10M 问题来了……</li>
<li>还有几篇可能有争议的文章，让你从不同的角度思考。
<ul>
<li><a href="https://idea.popcount.org/2017-01-06-select-is-fundamentally-broken/">Select is fundamentally broken</a></li>
<li><a href="https://idea.popcount.org/2017-02-20-epoll-is-fundamentally-broken-12/">Epoll is fundamentally broken 1/2</a></li>
<li><a href="https://idea.popcount.org/2017-03-20-epoll-is-fundamentally-broken-22/">Epoll is fundamentally broken 2/2</a></li>
</ul>
</li>
</ul>
<h1>Lock-Free 编程相关</h1>
<p>Lock-Free - 无锁技术越来越被开发人员重视，因为锁对于性能的影响实在是太大了，所以如果想开发出一个高性能的程序，你就非常有必要学习 Lock-Free 的编程方式。</p>
<p>关于无锁的数据结构，有几篇教程你可以看一下。</p>
<ul>
<li><a href="http://www.drdobbs.com/lock-free-data-structures/184401865">Dr.Dobb’s: Lock-Free Data Structures</a></li>
<li><a href="https://erdani.com/publications/cuj-2004-10.pdf">Andrei Alexandrescu: Lock-Free Data Structures</a></li>
</ul>
<p>然后强烈推荐一本免费的电子书：<a href="https://www.kernel.org/pub/linux/kernel/people/paulmck/perfbook/perfbook.html">Is Parallel Programming Hard, And, If So, What Can You Do About It?</a> ，这是大牛 <a href="https://www.linkedin.com/in/paulmckenney/">保罗·麦肯尼（Paul E. McKenney）</a> 写的书。这本书堪称并行编程的经典书，必看。</p>
<p>此时，Wikipedia 上有三个词条你要看一下，以此了解并发编程中的一些概念：<a href="https://en.wikipedia.org/wiki/Non-blocking_algorithm">Non-blocking algorithm</a> 、<a href="https://en.wikipedia.org/wiki/Read-copy-update">Read-copy-update</a> 和 <a href="https://en.wikipedia.org/wiki/Seqlock">Seqlock</a>。</p>
<p>接下来，读一下以下两篇论文 。</p>
<ul>
<li><a href="http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.53.8674&amp;rep=rep1&amp;type=pdf">Implementing Lock-Free Queues</a>， 这也是一篇很不错的论文，我把它介绍在了我的网站上 ，文章为“<a href="https://coolshell.cn/articles/8239.html">无锁队列的实现</a>”。</li>
<li><a href="http://www.cs.rochester.edu/~scott/papers/1996_PODC_queues.pdf">Simple, Fast, and Practical Non-Blocking and Blocking Concurrent Queue Algorithms</a> ，这篇论文给出了一个无阻塞和阻塞的并发队列算法。</li>
</ul>
<p>最后，有几个博客你要订阅一下。</p>
<ul>
<li><a href="http://www.1024cores.net/">1024cores</a> - 德米特里·伐由科夫（Dmitry Vyukov）的和 lock-free 编程相关的网站。</li>
<li><a href="https://paulmck.livejournal.com/">Paul E. McKenney</a> - 保罗（Paul）的个人网站。</li>
<li><a href="https://concurrencyfreaks.blogspot.com/">Concurrency Freaks</a> - 关于并发算法和相关模式的网站。</li>
<li><a href="http://preshing.com/">Preshing on Programming</a> - 加拿大程序员杰夫·普莱辛（Jeff Preshing）的技术博客，主要关注 C++ 和 Python 两门编程语言。他用 C++11 实现了类的反射机制，用 C++ 编写了 3D 小游戏 Hop Out，还为该游戏编写了一个游戏引擎。他还讨论了很多 C++ 的用法，比如 C++14 推荐的代码写法、新增的某些语言构造等，和 Python 很相似。阅读这个技术博客上的内容能够深深感受到博主对编程世界的崇敬和痴迷。</li>
<li><a href="http://herbsutter.com/">Sutter’s Mill</a> - 赫布·萨特（Herb Sutter）是一位杰出的 C++ 专家，曾担任 ISO C++ 标准委员会秘书和召集人超过 10 年。他的博客有关于 C++ 语言标准最新进展的信息，其中也有他的演讲视频。博客中还讨论了其他技术和 C++ 的差异，如 C# 和 JavaScript，它们的性能特点、怎样避免引入性能方面的缺陷等。</li>
<li><a href="https://mechanical-sympathy.blogspot.com/">Mechanical Sympathy</a> - 博主是马丁·汤普森（Martin Thompson），他是一名英国的技术极客，探索现代硬件的功能，并提供开发、培训、性能调优和咨询服务。他的博客主题是 Hardware and software working together in harmony，里面探讨了如何设计和编写软件使得它在硬件上能高性能地运行。非常值得一看。</li>
</ul>
<p>接下来，是一些编程相关的一些 C/C++ 的类库，这样你就不用从头再造轮子了（对于 Java 的，请参看 JDK 里的 Concurrent 开头的一系列的类）。</p>
<ul>
<li><a href="https://www.boost.org/doc/libs/1_60_0/doc/html/lockfree.html">Boost.Lockfree</a> - Boost 库中的无锁数据结构。</li>
<li><a href="https://github.com/concurrencykit/ck">ConcurrencyKit</a> - 并发性编程的原语。</li>
<li><a href="https://github.com/facebook/folly">Folly</a> - Facebook 的开源库（它对 MPMC 队列做了一个很好的实现）。</li>
<li><a href="https://github.com/preshing/junction">Junction</a> - C++ 中的并发数据结构。</li>
<li><a href="https://github.com/rigtorp/MPMCQueue">MPMCQueue</a> - 一个用 C++11 编写的有边界的“多生产者 - 多消费者”无锁队列。</li>
<li><a href="https://github.com/rigtorp/SPSCQueue">SPSCQueue</a> - 一个有边界的“单生产者 - 单消费者”的无等待、无锁的队列。</li>
<li><a href="https://github.com/rigtorp/Seqlock">Seqlock</a> - 用 C++ 实现的 Seqlock。</li>
<li><a href="http://liburcu.org/">Userspace RCU</a> - liburcu 是一个用户空间的 RCU（Read-copy-update，读 - 拷贝 - 更新）库。</li>
<li><a href="https://github.com/khizmax/libcds">libcds</a> - 一个并发数据结构的 C++ 库。</li>
<li><a href="https://liblfds.org/">liblfds</a> - 一个用 C 语言编写的可移植、无许可证、无锁的数据结构库。</li>
</ul>
<h1>其它</h1>
<ul>
<li>
<p>关于 64 位系统编程，只要去一个地方就行了： <a href="https://software.intel.com/en-us/blogs/2011/07/07/all-about-64-bit-programming-in-one-place/">All about 64-bit programming in one place</a>，这是一个关于 64 位编程相关的收集页面，其中包括相关的文章、28 节课程，还有知识库和相关的 blog。</p>
</li>
<li>
<p><a href="https://dl.acm.org/citation.cfm?id=3037750">What Scalable Programs Need from Transactional Memory</a> ，事务性内存（TM）一直是许多研究的重点，它在诸如 IBM Blue Gene/Q 和 Intel Haswell 等处理器中得到了支持。许多研究都使用 STAMP 基准测试套件来评估其设计。然而，我们所知的所有 TM 系统上的 STAMP 基准测试所获得的加速比较有限。</p>
<p>例如，在 IBM Blue Gene/Q 上有 64 个线程，我们观察到使用 Blue Gene/Q 硬件事务内存（HTM）的中值加速比为 1.4 倍，使用软件事务内存（STM）的中值加速比为 4.1 倍。什么限制了这些 TM 基准的性能？在本论文中，作者认为问题在于用于编写它们的编程模型和数据结构上，只要使用合适的模型和数据结构，程序的性能可以有 10 多倍的提升。</p>
</li>
<li>
<p><a href="https://software.intel.com/en-us/articles/improving-openssl-performance">Improving OpenSSL Performance</a> ，这篇文章除了教你如何提高 OpenSSL 的执行性能，还讲了一些底层的性能调优知识。</p>
</li>
<li>
<p>关于压缩的内容。为了避免枯燥，主要推荐下面这两篇实践性很强的文章。</p>
<ul>
<li><a href="https://www.ebayinc.com/stories/blogs/tech/how-ebays-shopping-cart-used-compression-techniques-to-solve-network-io-bottlenecks/">How eBay’s Shopping Cart used compression techniques to solve network I/O bottlenecks</a> ，这是一篇很好的文章，讲述了 eBay 是如何通过压缩数据来提高整体服务性能的，其中有几个比较好的压缩算法。除了可以让你学到相关的技术知识，还可以让你看到一种比较严谨的工程师文化。</li>
<li><a href="https://engineering.linkedin.com/blog/2017/05/boosting-site-speed-using-brotli-compression">Linkedin: Boosting Site Speed Using Brotli Compression</a> ，Linkedin 在 2017 年早些时候开始使用 <a href="https://en.wikipedia.org/wiki/Brotli">Brotli</a> 来替换 gzip，以此带来更快的访问，这篇文章讲述了什么是 Brotli 以及与其它压缩程序的比较和所带来的性能提升。</li>
</ul>
</li>
<li>
<p>这里有两篇关于 SSD 硬盘性能测试的文章。<a href="https://devs.mailchimp.com/blog/performance-testing-with-ssds-part-1/">Performance Testing with SSDs, Part 1</a> 和 <a href="https://devs.mailchimp.com/blog/performance-testing-with-ssds-pt-2/">Performance Testing with SSDs Part 2</a> ，这两篇文章介绍了测试 SSD 硬盘性能以及相关的操作系统调优方法。</p>
</li>
<li>
<p><a href="https://www.dwheeler.com/secure-programs/">Secure Programming HOWTO - Creating Secure Software</a> ，这是一本电子书，其中有繁体中文的翻译，这本电子书讲了 Linux/Unix 下的一些安全编程方面的知识。</p>
</li>
</ul>
<h1>相关论文</h1>
<ul>
<li>
<p><a href="https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/acrobat-17.pdf">Hints for Computer System Design</a> ，计算机设计的忠告，这是 ACM 图灵奖得主 <a href="https://en.wikipedia.org/wiki/Butler_Lampson">Butler Lampson</a> 在 Xerox PARC 工作时的一篇论文。这篇论文简明扼要地总结了他在做系统设计时的一些想法，非常值得一读。（用他的话来说，“Studying the design and implementation of a number of computer has led to some general hints for system design. They are described here and illustrated by many examples, ranging from hardware such as the Alto and the Dorado to application programs such as Bravo and Star“。）</p>
</li>
<li>
<p><a href="http://www.hpl.hp.com/techreports/tandem/TR-86.1.pdf">The 5 minute rule for trading memory for disc accesses and the 5 byte rule for trading memory for CPU time</a> ，根据文章名称也可以看出，5 分钟法则是用来衡量内存与磁盘的，而 5 字节法则则是在内存和 CPU 之间的权衡。这两个法则是 Jim Gray 和 Franco Putzolu 在 1986 年的文章。</p>
<p>在该论文发表 10 年后的 1997 年，Jim Gray 和 Goetz Graefe 又在 <a href="http://research.microsoft.com/en-us/um/people/gray/5_min_rule_SIGMOD.pdf">The Five-Minute Rule Ten Years Later and Other Computer Storage Rules of Thumb</a> 中对该法则进行了重新审视。2007 年，也就是该论文发表 20 年后，这年的 1 月 28 日，Jim Gray 驾驶一艘 40 英尺长的船从旧金山港出海，目的是航行到附近的费拉隆岛，在那里撒下母亲的骨灰。出海之后，他就同朋友和亲属失去了联系。为了纪念和向大师致敬，时隔 10 多年后的 2009 年 Goetz Graefe 又发表了 <a href="https://cacm.acm.org/magazines/2009/7/32091-the-five-minute-rule-20-years-later/fulltext">The Five-Minute Rule 20 Years Later (and How Falsh Memory Changes the Rules)</a>。</p>
<p>注明一下，Jim Gray，关系型、数据库领域大师。因在数据库和事务处理研究和实现方面的开创性贡献而获得 1998 年图灵奖。美国科学院、工程院两院院士，ACM 和 IEEE 两会会士。他 25 岁成为加州大学伯克利分校计算机科学学院第一位博士。在 IBM 工作期间参与和主持了 IMS、System R、SQL／DS、DB2 等项目的开发。后任职于微软研究院，主要关注应用数据库技术来处理各学科的海量信息。</p>
</li>
</ul>
<h1>小结</h1>
<p>好了，总结一下今天的内容。异步 I/O 模型是我个人觉得所有程序员都必需要学习的一门技术或是编程方法，这其中的设计模式或是解决方法可以借鉴到分布式架构上来。而且我认为，学习这些模型非常重要，你千万要认真学习。</p>
<p>接下来是 Lock-Free 方面的内容，由于锁对于性能的影响实在是太大了，所以它越来越被开发人员所重视。如果想开发出一个高性能的程序，你非常有必要学习 Lock-Free 的编程方式。随后，我给出系统底层方面的其它一些重要知识，如 64 位编程、提高 OpenSSL 的执行性能、压缩、SSD 硬盘性能测试等。最后介绍了几篇我认为对学习和巩固这些知识非常有帮助的论文，都很经典，推荐你务必看看。</p>
<p>下篇文章是数据库方面的内容，我们将探讨各种类型的数据库，非常有意思。敬请期待。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="077&#32;&#32;程序员练级攻略（2018）：Linux系统、内存和网络.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="079&#32;&#32;程序员练级攻略（2018）：Java底层知识.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4354423a8d645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
</body>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-NPSEEVD756"></script>
<script>
    window.dataLayer = window.dataLayer || [];

    function gtag() {
        dataLayer.push(arguments);
    }

    gtag('js', new Date());
    gtag('config', 'G-NPSEEVD756');
    var path = window.location.pathname
    var cookie = getCookie("lastPath");
    console.log(path)
    if (path.replace("/", "") === "") {
        if (cookie.replace("/", "") !== "") {
            console.log(cookie)
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E5%B7%A6%E8%80%B3%E5%90%AC%E9%A3%8E/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
        }
    } else {
        setCookie("lastPath", path)
    }

    function setCookie(cname, cvalue) {
        var d = new Date();
        d.setTime(d.getTime() + (180 * 24 * 60 * 60 * 1000));
        var expires = "expires=" + d.toGMTString();
        document.cookie = cname + "=" + cvalue + "; " + expires + ";path = /";
    }

    function getCookie(cname) {
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i].trim();
            if (c.indexOf(name) === 0) return c.substring(name.length, c.length);
        }
        return "";
    }
</script>

</html>
