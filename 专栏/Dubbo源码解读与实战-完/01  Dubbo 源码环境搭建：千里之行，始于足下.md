<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>01  Dubbo 源码环境搭建：千里之行，始于足下.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;深入掌握&#32;Dubbo&#32;原理与实现，提升你的职场竞争力.md">00 开篇词  深入掌握 Dubbo 原理与实现，提升你的职场竞争力.md</a>

                </li>
                <li>

                    <a class="current-tab" href="01&#32;&#32;Dubbo&#32;源码环境搭建：千里之行，始于足下.md">01  Dubbo 源码环境搭建：千里之行，始于足下.md</a>
                    

                </li>
                <li>

                    
                    <a href="02&#32;Dubbo&#32;的配置总线：抓住&#32;URL，就理解了半个&#32;Dubbo.md">02 Dubbo 的配置总线：抓住 URL，就理解了半个 Dubbo.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;Dubbo&#32;SPI&#32;精析，接口实现两极反转（上）.md">03  Dubbo SPI 精析，接口实现两极反转（上）.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;Dubbo&#32;SPI&#32;精析，接口实现两极反转（下）.md">04  Dubbo SPI 精析，接口实现两极反转（下）.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;海量定时任务，一个时间轮搞定.md">05  海量定时任务，一个时间轮搞定.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;ZooKeeper&#32;与&#32;Curator，求你别用&#32;ZkClient&#32;了（上）.md">06  ZooKeeper 与 Curator，求你别用 ZkClient 了（上）.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;ZooKeeper&#32;与&#32;Curator，求你别用&#32;ZkClient&#32;了（下）.md">07  ZooKeeper 与 Curator，求你别用 ZkClient 了（下）.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;代理模式与常见实现.md">08  代理模式与常见实现.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;Netty&#32;入门，用它做网络编程都说好（上）.md">09  Netty 入门，用它做网络编程都说好（上）.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;Netty&#32;入门，用它做网络编程都说好（下）.md">10  Netty 入门，用它做网络编程都说好（下）.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;简易版&#32;RPC&#32;框架实现（上）.md">11  简易版 RPC 框架实现（上）.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;简易版&#32;RPC&#32;框架实现（下）.md">12  简易版 RPC 框架实现（下）.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;本地缓存：降低&#32;ZooKeeper&#32;压力的一个常用手段.md">13  本地缓存：降低 ZooKeeper 压力的一个常用手段.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;重试机制是网络操作的基本保证.md">14  重试机制是网络操作的基本保证.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;ZooKeeper&#32;注册中心实现，官方推荐注册中心实践.md">15  ZooKeeper 注册中心实现，官方推荐注册中心实践.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;Dubbo&#32;Serialize&#32;层：多种序列化算法，总有一款适合你.md">16  Dubbo Serialize 层：多种序列化算法，总有一款适合你.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;Dubbo&#32;Remoting&#32;层核心接口分析：这居然是一套兼容所有&#32;NIO&#32;框架的设计？.md">17  Dubbo Remoting 层核心接口分析：这居然是一套兼容所有 NIO 框架的设计？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;Buffer&#32;缓冲区：我们不生产数据，我们只是数据的搬运工.md">18  Buffer 缓冲区：我们不生产数据，我们只是数据的搬运工.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;Transporter&#32;层核心实现：编解码与线程模型一文打尽（上）.md">19  Transporter 层核心实现：编解码与线程模型一文打尽（上）.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;Transporter&#32;层核心实现：编解码与线程模型一文打尽（下）.md">20  Transporter 层核心实现：编解码与线程模型一文打尽（下）.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;Exchange&#32;层剖析：彻底搞懂&#32;Request-Response&#32;模型（上）.md">21  Exchange 层剖析：彻底搞懂 Request-Response 模型（上）.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;Exchange&#32;层剖析：彻底搞懂&#32;Request-Response&#32;模型（下）.md">22  Exchange 层剖析：彻底搞懂 Request-Response 模型（下）.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;核心接口介绍，RPC&#32;层骨架梳理.md">23  核心接口介绍，RPC 层骨架梳理.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;从&#32;Protocol&#32;起手，看服务暴露和服务引用的全流程（上）.md">24  从 Protocol 起手，看服务暴露和服务引用的全流程（上）.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;从&#32;Protocol&#32;起手，看服务暴露和服务引用的全流程（下）.md">25  从 Protocol 起手，看服务暴露和服务引用的全流程（下）.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;&#32;加餐：直击&#32;Dubbo&#32;“心脏”，带你一起探秘&#32;Invoker（上）.md">26  加餐：直击 Dubbo “心脏”，带你一起探秘 Invoker（上）.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;&#32;加餐：直击&#32;Dubbo&#32;“心脏”，带你一起探秘&#32;Invoker（下）.md">27  加餐：直击 Dubbo “心脏”，带你一起探秘 Invoker（下）.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;&#32;复杂问题简单化，代理帮你隐藏了多少底层细节？.md">28  复杂问题简单化，代理帮你隐藏了多少底层细节？.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Dubbo%E6%BA%90%E7%A0%81%E8%A7%A3%E8%AF%BB%E4%B8%8E%E5%AE%9E%E6%88%98-%E5%AE%8C/29%20%20%E5%8A%A0%E9%A4%90%EF%BC%9AHTTP%20%E5%8D%8F%E8%AE%AE%20+%20JSON-RPC%EF%BC%8CDubbo%20%E8%B7%A8%E8%AF%AD%E8%A8%80%E5%B0%B1%E6%98%AF%E5%A6%82%E6%AD%A4%E7%AE%80%E5%8D%95.md">29  加餐：HTTP 协议 + JSON-RPC，Dubbo 跨语言就是如此简单.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;&#32;Filter&#32;接口，扩展&#32;Dubbo&#32;框架的常用手段指北.md">30  Filter 接口，扩展 Dubbo 框架的常用手段指北.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;&#32;加餐：深潜&#32;Directory&#32;实现，探秘服务目录玄机.md">31  加餐：深潜 Directory 实现，探秘服务目录玄机.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;&#32;路由机制：请求到底怎么走，它说了算（上）.md">32  路由机制：请求到底怎么走，它说了算（上）.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;&#32;路由机制：请求到底怎么走，它说了算（下）.md">33  路由机制：请求到底怎么走，它说了算（下）.md</a>

                </li>
                <li>

                    
                    <a href="34&#32;&#32;加餐：初探&#32;Dubbo&#32;动态配置的那些事儿.md">34  加餐：初探 Dubbo 动态配置的那些事儿.md</a>

                </li>
                <li>

                    
                    <a href="35&#32;&#32;负载均衡：公平公正物尽其用的负载均衡策略，这里都有（上）.md">35  负载均衡：公平公正物尽其用的负载均衡策略，这里都有（上）.md</a>

                </li>
                <li>

                    
                    <a href="36&#32;&#32;负载均衡：公平公正物尽其用的负载均衡策略，这里都有（下）.md">36  负载均衡：公平公正物尽其用的负载均衡策略，这里都有（下）.md</a>

                </li>
                <li>

                    
                    <a href="37&#32;&#32;集群容错：一个好汉三个帮（上）.md">37  集群容错：一个好汉三个帮（上）.md</a>

                </li>
                <li>

                    
                    <a href="38&#32;&#32;集群容错：一个好汉三个帮（下）.md">38  集群容错：一个好汉三个帮（下）.md</a>

                </li>
                <li>

                    
                    <a href="39&#32;&#32;加餐：多个返回值不用怕，Merger&#32;合并器来帮忙.md">39  加餐：多个返回值不用怕，Merger 合并器来帮忙.md</a>

                </li>
                <li>

                    
                    <a href="40&#32;&#32;加餐：模拟远程调用，Mock&#32;机制帮你搞定.md">40  加餐：模拟远程调用，Mock 机制帮你搞定.md</a>

                </li>
                <li>

                    
                    <a href="41&#32;&#32;加餐：一键通关服务发布全流程.md">41  加餐：一键通关服务发布全流程.md</a>

                </li>
                <li>

                    
                    <a href="42&#32;&#32;加餐：服务引用流程全解析.md">42  加餐：服务引用流程全解析.md</a>

                </li>
                <li>

                    
                    <a href="43&#32;&#32;服务自省设计方案：新版本新方案.md">43  服务自省设计方案：新版本新方案.md</a>

                </li>
                <li>

                    
                    <a href="44&#32;&#32;元数据方案深度剖析，如何避免注册中心数据量膨胀？.md">44  元数据方案深度剖析，如何避免注册中心数据量膨胀？.md</a>

                </li>
                <li>

                    
                    <a href="45&#32;&#32;加餐：深入服务自省方案中的服务发布订阅（上）.md">45  加餐：深入服务自省方案中的服务发布订阅（上）.md</a>

                </li>
                <li>

                    
                    <a href="46&#32;&#32;加餐：深入服务自省方案中的服务发布订阅（下）.md">46  加餐：深入服务自省方案中的服务发布订阅（下）.md</a>

                </li>
                <li>

                    
                    <a href="47&#32;&#32;配置中心设计与实现：集中化配置&#32;and&#32;本地化配置，我都要（上）.md">47  配置中心设计与实现：集中化配置 and 本地化配置，我都要（上）.md</a>

                </li>
                <li>

                    
                    <a href="48&#32;&#32;配置中心设计与实现：集中化配置&#32;and&#32;本地化配置，我都要（下）.md">48  配置中心设计与实现：集中化配置 and 本地化配置，我都要（下）.md</a>

                </li>
                <li>

                    
                    <a href="49&#32;结束语&#32;&#32;认真学习，缩小差距.md">49 结束语  认真学习，缩小差距.md</a>

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
                        <div><h1>01  Dubbo 源码环境搭建：千里之行，始于足下</h1>
<p><strong>好的开始是成功的一半，阅读源码也是一样。</strong> 很多同学在下定决心阅读一个开源框架之后，就一头扎进去，迷失在代码“迷宫”中。此时，有同学意识到，需要一边 Debug 一边看；然后又有一批同学在搭建源码环境的时候兜兜转转，走上了放弃之路；最后剩下为数不多的同学，搭建完了源码环境，却又不知道如何模拟请求让源码执行到自己想要 Debug 的地方。</p>
<p>以上这些痛点问题你是不是很熟悉？是不是也曾遇到过？没关系，本课时我就来手把手带领你搭建 Dubbo 源码环境。</p>
<ul>
<li>在开始搭建源码环境之前，我们会先整体过一下 Dubbo 的架构，这可以帮助你了解 Dubbo 的基本功能以及核心角色。</li>
<li>之后我们再动手搭建 Dubbo 源码环境，构建一个 Demo 示例可运行的最简环境。</li>
<li>完成源码环境搭建之后，我们还会深入介绍 Dubbo 源码中各个核心模块的功能，这会为后续分析各个模块的实现做铺垫。</li>
<li>最后，我们再详细分析下 Dubbo 源码自带的三个 Demo 示例，简单回顾一下 Dubbo 的基本用法，这三个示例也将是我们后续 Debug 源码的入口。</li>
</ul>
<h3>Dubbo 架构简介</h3>
<p>为便于你更好理解和学习，在开始搭建 Dubbo 源码环境之前，我们先来简单介绍一下 Dubbo 架构中的核心角色，帮助你简单回顾一下 Dubbo 的架构，也帮助不熟悉 Dubbo 的小伙伴快速了解 Dubbo。下图展示了 Dubbo 核心架构：</p>
<p><img src="assets/CgqCHl8eRaCAW4-LAAB7_C-aKWA601.png" alt="Drawing 0.png" /></p>
<p>Dubbo 核心架构图</p>
<ul>
<li><strong>Registry：注册中心。</strong> 负责服务地址的注册与查找，服务的 Provider 和 Consumer 只在启动时与注册中心交互。注册中心通过长连接感知 Provider 的存在，在 Provider 出现宕机的时候，注册中心会立即推送相关事件通知 Consumer。</li>
<li><strong>Provider：服务提供者。</strong> 在它启动的时候，会向 Registry 进行注册操作，将自己服务的地址和相关配置信息封装成 URL 添加到 ZooKeeper 中。</li>
<li><strong>Consumer：服务消费者。</strong> 在它启动的时候，会向 Registry 进行订阅操作。订阅操作会从 ZooKeeper 中获取 Provider 注册的 URL，并在 ZooKeeper 中添加相应的监听器。获取到 Provider URL 之后，Consumer 会根据负载均衡算法从多个 Provider 中选择一个 Provider 并与其建立连接，最后发起对 Provider 的 RPC 调用。 如果 Provider URL 发生变更，Consumer 将会通过之前订阅过程中在注册中心添加的监听器，获取到最新的 Provider URL 信息，进行相应的调整，比如断开与宕机 Provider 的连接，并与新的 Provider 建立连接。Consumer 与 Provider 建立的是长连接，且 Consumer 会缓存 Provider 信息，所以一旦连接建立，即使注册中心宕机，也不会影响已运行的 Provider 和 Consumer。</li>
<li><strong>Monitor：监控中心。</strong> 用于统计服务的调用次数和调用时间。Provider 和 Consumer 在运行过程中，会在内存中统计调用次数和调用时间，定时每分钟发送一次统计数据到监控中心。监控中心在上面的架构图中并不是必要角色，监控中心宕机不会影响 Provider、Consumer 以及 Registry 的功能，只会丢失监控数据而已。</li>
</ul>
<h3>搭建Dubbo源码环境</h3>
<p>当然，要搭建Dubbo 源码环境，你首先需要下载源码。这里你可以直接从官方仓库 <a href="https://github.com/apache/dubbo">https://github.com/apache/dubbo</a>Fork 到自己的仓库，直接执行下面的命令去下载代码：</p>
<pre><code>git clone <a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="b0d7d9c4f0d7d9c4d8c5d29ed3dfdd">[email&#160;protected]</a>:xxxxxxxx/dubbo.git 
</code></pre>
<p>然后切换分支，因为目前最新的是 Dubbo 2.7.7 版本，所以这里我们就用这个新版本：</p>
<pre><code>git checkout -b dubbo-2.7.7 dubbo-2.7.7 
</code></pre>
<p>接下来，执行 mvn 命令进行编译：</p>
<pre><code>mvn clean install -Dmaven.test.skip=true 
</code></pre>
<p>最后，执行下面的命令转换成 IDEA 项目：</p>
<pre><code>mvn idea:idea // 要是执行报错，就执行这个 mvn idea:workspace 
</code></pre>
<p>然后，在 IDEA 中导入源码，因为这个导入过程中会下载所需的依赖包，所以会耗费点时间。</p>
<h3>Dubbo源码核心模块</h3>
<p>在 IDEA 成功导入 Dubbo 源码之后，你看到的项目结构如下图所示：</p>
<p><img src="assets/Ciqc1F8eRcOAdzNmAADHxcenG7I722.png" alt="Drawing 2.png" /></p>
<p>下面我们就来简单介绍一下这些核心模块的功能，至于详细分析，在后面的课时中我们还会继续讲解。</p>
<ul>
<li><strong>dubbo-common 模块：</strong> Dubbo 的一个公共模块，其中有很多工具类以及公共逻辑，例如课程后面紧接着要介绍的 Dubbo SPI 实现、时间轮实现、动态编译器等。</li>
</ul>
<p><img src="assets/CgqCHl8eRfWANQSTAAHowsC6F8s134.png" alt="Drawing 4.png" /></p>
<ul>
<li><strong>dubbo-remoting 模块：</strong> Dubbo 的远程通信模块，其中的子模块依赖各种开源组件实现远程通信。在 dubbo-remoting-api 子模块中定义该模块的抽象概念，在其他子模块中依赖其他开源组件进行实现，例如，dubbo-remoting-netty4 子模块依赖 Netty 4 实现远程通信，dubbo-remoting-zookeeper 通过 Apache Curator 实现与 ZooKeeper 集群的交互。</li>
</ul>
<p><img src="assets/Ciqc1F8eRgCAR30EAABc4PYop3w206.png" alt="Drawing 5.png" /></p>
<ul>
<li><strong>dubbo-rpc 模块：</strong> Dubbo 中对远程调用协议进行抽象的模块，其中抽象了各种协议，依赖于 dubbo-remoting 模块的远程调用功能。dubbo-rpc-api 子模块是核心抽象，其他子模块是针对具体协议的实现，例如，dubbo-rpc-dubbo 子模块是对 Dubbo 协议的实现，依赖了 dubbo-remoting-netty4 等 dubbo-remoting 子模块。 dubbo-rpc 模块的实现中只包含一对一的调用，不关心集群的相关内容。</li>
</ul>
<p><img src="assets/Ciqc1F8eRguAA8jOAABqHomePJk138.png" alt="Drawing 6.png" /></p>
<ul>
<li><strong>dubbo-cluster 模块：</strong> Dubbo 中负责管理集群的模块，提供了负载均衡、容错、路由等一系列集群相关的功能，最终的目的是将多个 Provider 伪装为一个 Provider，这样 Consumer 就可以像调用一个 Provider 那样调用 Provider 集群了。</li>
<li><strong>dubbo-registry 模块：</strong> Dubbo 中负责与多种开源注册中心进行交互的模块，提供注册中心的能力。其中， dubbo-registry-api 子模块是顶层抽象，其他子模块是针对具体开源注册中心组件的具体实现，例如，dubbo-registry-zookeeper 子模块是 Dubbo 接入 ZooKeeper 的具体实现。</li>
</ul>
<p><img src="assets/CgqCHl8eRhWANEiTAAB2ATuQ2vc619.png" alt="Drawing 7.png" /></p>
<ul>
<li><strong>dubbo-monitor 模块：</strong> Dubbo 的监控模块，主要用于统计服务调用次数、调用时间以及实现调用链跟踪的服务。</li>
<li><strong>dubbo-config 模块：</strong> Dubbo 对外暴露的配置都是由该模块进行解析的。例如，dubbo-config-api 子模块负责处理 API 方式使用时的相关配置，dubbo-config-spring 子模块负责处理与 Spring 集成使用时的相关配置方式。有了 dubbo-config 模块，用户只需要了解 Dubbo 配置的规则即可，无须了解 Dubbo 内部的细节。</li>
</ul>
<p><img src="assets/CgqCHl8eRhyAVJ43AAAaPAwMeQ4525.png" alt="Drawing 8.png" /></p>
<ul>
<li><strong>dubbo-metadata 模块：</strong> Dubbo 的元数据模块（本课程后续会详细介绍元数据的内容）。dubbo-metadata 模块的实现套路也是有一个 api 子模块进行抽象，然后其他子模块进行具体实现。</li>
</ul>
<p><img src="assets/CgqCHl8eRiSAPFIYAABXCRqgsNA891.png" alt="Drawing 9.png" /></p>
<ul>
<li><strong>dubbo-configcenter 模块：</strong> Dubbo 的动态配置模块，主要负责外部化配置以及服务治理规则的存储与通知，提供了多个子模块用来接入多种开源的服务发现组件。</li>
</ul>
<p><img src="assets/CgqCHl8eRiuAM7LfAAA9BmMR2zY483.png" alt="Drawing 10.png" /></p>
<h3>Dubbo 源码中的 Demo 示例</h3>
<p>在 Dubbo 源码中我们可以看到一个 dubbo-demo 模块，共包括三个非常基础 的 Dubbo 示例项目，分别是： <strong>使用 XML 配置的 Demo 示例、使用注解配置的 Demo 示例</strong> 以及 <strong>直接使用 API 的 Demo 示例</strong> 。下面我们将从这三个示例的角度，简单介绍 Dubbo 的基本使用。同时，这三个项目也将作为后续 Debug Dubbo 源码的入口，我们会根据需要在其之上进行修改 。不过在这儿之前，你需要先启动 ZooKeeper 作为注册中心，然后编写一个业务接口作为 Provider 和 Consumer 的公约。</p>
<h4>启动 ZooKeeper</h4>
<p>在前面 Dubbo 的架构图中，你可以看到 Provider 的地址以及配置信息是通过注册中心传递给 Consumer 的。 Dubbo 支持的注册中心尽管有很多， 但在生产环境中， <strong>基本都是用 ZooKeeper 作为注册中心</strong> 。因此，在调试 Dubbo 源码时，自然需要在本地启动 ZooKeeper。</p>
<p>那怎么去启动 ZooKeeper 呢？</p>
<p>首先，你得下载 zookeeper-3.4.14.tar.gz 包（下载地址： <a href="https://archive.apache.org/dist/zookeeper/zookeeper-3.4.14/">https://archive.apache.org/dist/zookeeper/zookeeper-3.4.14/</a>）。下载完成之后执行如下命令解压缩：</p>
<pre><code>tar -zxf zookeeper-3.4.14.tar.gz 
</code></pre>
<p>解压完成之后，进入 zookeeper-3.4.14 目录，复制 conf/zoo_sample.cfg 文件并重命名为 conf/zoo.cfg，之后执行如下命令就可以启动 ZooKeeper了。</p>
<pre><code>&gt;./bin/zkServer.sh start 

# 下面为输出内容 

ZooKeeper JMX enabled by default 

Using config: /Users/xxx/zookeeper-3.4.14/bin/../conf/zoo.cfg # 配置文件 

Starting zookeeper ... STARTED # 启动成功 
</code></pre>
<h4>业务接口</h4>
<p>在使用 Dubbo 之前，你还需要一个业务接口，这个业务接口可以认为是 Dubbo Provider 和 Dubbo Consumer 的公约，反映出很多信息：</p>
<ul>
<li>Provider ，如何提供服务、提供的服务名称是什么、需要接收什么参数、需要返回什么响应；</li>
<li>Consumer ，如何使用服务、使用的服务名称是什么、需要传入什么参数、会得到什么响应。</li>
</ul>
<p>dubbo-demo-interface 模块就是定义业务接口的地方，如下图所示：</p>
<p><img src="assets/CgqCHl8eRlWAPwvCAACx42Xn9Dk409.png" alt="Drawing 11.png" /></p>
<p>其中，DemoService 接口中定义了两个方法：</p>
<pre><code>public interface DemoService { 

    String sayHello(String name); // 同步调用 

    // 异步调用 

    default CompletableFuture&lt;String&gt; sayHelloAsync(String name) {  

        return CompletableFuture.completedFuture(sayHello(name)); 

    } 

} 
</code></pre>
<h4>Demo 1：基于 XML 配置</h4>
<p>在 dubbo-demo 模块下的 dubbo-demo-xml 模块，提供了基于 Spring XML 的 Provider 和 Consumer。</p>
<p>我们先来看 dubbo-demo-xml-provider 模块，其结构如下图所示：</p>
<p><img src="assets/CgqCHl8eRmKAT8LjAADV8C5fM8E391.png" alt="Drawing 12.png" /></p>
<p>在其 pom.xml 中除了一堆 dubbo 的依赖之外，还有依赖了 DemoService 这个公共接口：</p>
<pre><code>&lt;dependency&gt; 

    &lt;groupId&gt;org.apache.dubbo&lt;/groupId&gt; 

    &lt;artifactId&gt;dubbo-demo-interface&lt;/artifactId&gt; 

    &lt;version&gt;${project.parent.version}&lt;/version&gt; 

&lt;/dependency&gt; 
</code></pre>
<p>DemoServiceImpl 实现了 DemoService 接口，sayHello() 方法直接返回一个字符串，sayHelloAsync() 方法返回一个 CompletableFuture 对象。</p>
<p>在 dubbo-provider.xml 配置文件中，会将 DemoServiceImpl 配置成一个 Spring Bean，并作为 DemoService 服务暴露出去：</p>
<pre><code>&lt;!-- 配置为 Spring Bean --&gt; 

&lt;bean id=&quot;demoService&quot; class=&quot;org.apache.dubbo.demo.provider.DemoServiceImpl&quot;/&gt; 

&lt;!-- 作为 Dubbo 服务暴露出去 --&gt; 

&lt;dubbo:service interface=&quot;org.apache.dubbo.demo.DemoService&quot; ref=&quot;demoService&quot;/&gt; 
</code></pre>
<p>还有就是指定注册中心地址（就是前面 ZooKeeper 的地址），这样 Dubbo 才能把暴露的 DemoService 服务注册到 ZooKeeper 中：</p>
<pre><code>&lt;!-- Zookeeper 地址 --&gt; 

&lt;dubbo:registry address=&quot;zookeeper://127.0.0.1:2181&quot;/&gt; 
</code></pre>
<p>最后，在 Application 中写个 main() 方法，指定 Spring 配置文件并启动 ClassPathXmlApplicationContext 即可。</p>
<p>接下来再看 dubbo-demo-xml-consumer 模块，结构如下图所示：</p>
<p><img src="assets/Ciqc1F8eRnuAWnTAAAE7eBUfEoA405.png" alt="Drawing 13.png" /></p>
<p>在 pom.xml 中同样依赖了 dubbo-demo-interface 这个公共模块。</p>
<p>在 dubbo-consumer.xml 配置文件中，会指定注册中心地址（就是前面 ZooKeeper 的地址），这样 Dubbo 才能从 ZooKeeper 中拉取到 Provider 暴露的服务列表信息：</p>
<pre><code>&lt;!-- Zookeeper地址 --&gt; 

&lt;dubbo:registry address=&quot;zookeeper://127.0.0.1:2181&quot;/&gt; 
</code></pre>
<p>还会使用 <a href="dubbo:reference">dubbo:reference</a> 引入 DemoService 服务，后面可以作为 Spring Bean 使用：</p>
<pre><code>&lt;!--引入DemoService服务，并配置成Spring Bean--&gt; 

&lt;dubbo:reference id=&quot;demoService&quot; check=&quot;false&quot;  

                 interface=&quot;org.apache.dubbo.demo.DemoService&quot;/&gt; 
</code></pre>
<p>最后，在 Application 中写个 main() 方法，指定 Spring 配置文件并启动 ClassPathXmlApplicationContext 之后，就可以远程调用 Provider 端的 DemoService 的 sayHello() 方法了。</p>
<h4>Demo 2：基于注解配置</h4>
<p>dubbo-demo-annotation 模块是基于 Spring 注解配置的示例，无非就是将 XML 的那些配置信息转移到了注解上。</p>
<p>我们先来看 dubbo-demo-annotation-provider 这个示例模块：</p>
<pre><code>public class Application { 

    public static void main(String[] args) throws Exception { 

	    // 使用AnnotationConfigApplicationContext初始化Spring容器， 

        // 从ProviderConfiguration这个类的注解上拿相关配置信息 

        AnnotationConfigApplicationContext context =  

              new AnnotationConfigApplicationContext( 

                  ProviderConfiguration.class); 

        context.start(); 

        System.in.read(); 

    } 

    @Configuration // 配置类 

    // @EnableDubbo注解指定包下的Bean都会被扫描，并做Dubbo服务暴露出去 

    @EnableDubbo(scanBasePackages = &quot;org.apache.dubbo.demo.provider&quot;)      

    // @PropertySource注解指定了其他配置信息 

    @PropertySource(&quot;classpath:/spring/dubbo-provider.properties&quot;)      

    static class ProviderConfiguration { 

        @Bean 

        public RegistryConfig registryConfig() { 

            RegistryConfig registryConfig = new RegistryConfig(); 

            registryConfig.setAddress(&quot;zookeeper://127.0.0.1:2181&quot;); 

            return registryConfig; 

        } 

    } 

} 
</code></pre>
<p>这里，同样会有一个 DemoServiceImpl 实现了 DemoService 接口，并且在 org.apache.dubbo.demo.provider 目录下，能被扫描到，暴露成 Dubbo 服务。</p>
<p>接着再来看 dubbo-demo-annotation-consumer 模块，其中 Application 中也是通过 AnnotationConfigApplicationContext 初始化 Spring 容器，也会扫描指定目录下的 Bean，会扫到 DemoServiceComponent 这个 Bean，其中就通过 @Reference 注解注入 Dubbo 服务相关的 Bean：</p>
<pre><code>@Component(&quot;demoServiceComponent&quot;) 

public class DemoServiceComponent implements DemoService { 

    @Reference // 注入Dubbo服务 

    private DemoService demoService; 

    @Override 

    public String sayHello(String name) { 

        return demoService.sayHello(name); 

    } 

	  // 其他方法 

} 
</code></pre>
<h4>Demo 3：基于 API 配置</h4>
<p>在有的场景中，不能依赖于 Spring 框架，只能使用 API 来构建 Dubbo Provider 和 Consumer，比较典型的一种场景就是在写 SDK 的时候。</p>
<p>先来看 dubbo-demo-api-provider 模块，其中 Application.main() 方法是入口：</p>
<pre><code>// 创建一个ServiceConfig的实例，泛型参数是业务接口实现类， 

// 即DemoServiceImpl 

ServiceConfig&lt;DemoServiceImpl&gt; service = new ServiceConfig&lt;&gt;(); 

// 指定业务接口 

service.setInterface(DemoService.class); 

// 指定业务接口的实现，由该对象来处理Consumer的请求 

service.setRef(new DemoServiceImpl()); 

// 获取DubboBootstrap实例，这是个单例的对象 

DubboBootstrap bootstrap = DubboBootstrap.getInstance(); 

//生成一个 ApplicationConfig 的实例、指定ZK地址以及ServiceConfig实例 

bootstrap.application(new ApplicationConfig(&quot;dubbo-demo-api-provider&quot;)) 

        .registry(new RegistryConfig(&quot;zookeeper://127.0.0.1:2181&quot;)) 

        .service(service) 

        .start() 

        .await(); 
</code></pre>
<p>这里，同样会有一个 DemoServiceImpl 实现了 DemoService 接口，并且在 org.apache.dubbo.demo.provider 目录下，能被扫描到，暴露成 Dubbo 服务。</p>
<p>再来看 dubbo-demo-api-consumer 模块，其中 Application 中包含一个普通的 main() 方法入口：</p>
<pre><code> // 创建ReferenceConfig,其中指定了引用的接口DemoService 

 ReferenceConfig&lt;DemoService&gt; reference = new ReferenceConfig&lt;&gt;(); 

 reference.setInterface(DemoService.class); 

 reference.setGeneric(&quot;true&quot;); 

  

 // 创建DubboBootstrap，指定ApplicationConfig以及RegistryConfig 

 DubboBootstrap bootstrap = DubboBootstrap.getInstance(); 

 bootstrap.application(new ApplicationConfig(&quot;dubbo-demo-api-consumer&quot;)) 

         .registry(new RegistryConfig(&quot;zookeeper://127.0.0.1:2181&quot;)) 

         .reference(reference) 

         .start(); 

 // 获取DemoService实例并调用其方法 

 DemoService demoService = ReferenceConfigCache.getCache() 

    .get(reference); 

 String message = demoService.sayHello(&quot;dubbo&quot;); 

 System.out.println(message); 
</code></pre>
<h3>总结</h3>
<p>在本课时，我们首先介绍了 Dubbo 的核心架构以及各核心组件的功能，接下来又搭建了 Dubbo 源码环境，并详细介绍了 Dubbo 核心模块的功能，为后续分析 Dubbo 源码打下了基础。最后我们还深入分析了 Dubbo 源码中自带的三个 Demo 示例，现在你就可以以这三个 Demo 示例为入口 Debug Dubbo 源码了。</p>
<p>在后面的课时中，我们将解决几个问题：Dubbo 是如何与 ZooKeeper 等注册中心进行交互的？Provider 与 Consumer 之间是如何交互的？为什么我们在编写业务代码的时候，感受不到任何网络交互？Dubbo Provider 发布到注册中心的数据是什么？Consumer 为何能正确识别？两者的统一契约是什么？这个契约是如何做到可扩展的？这个契约还会用在 Dubbo 的哪些地方？这些问题你也可以提前思考一下，在后面的课程中我会一一为你解答。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="00&#32;开篇词&#32;&#32;深入掌握&#32;Dubbo&#32;原理与实现，提升你的职场竞争力.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="02&#32;Dubbo&#32;的配置总线：抓住&#32;URL，就理解了半个&#32;Dubbo.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433ed72b2970ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Dubbo%E6%BA%90%E7%A0%81%E8%A7%A3%E8%AF%BB%E4%B8%8E%E5%AE%9E%E6%88%98-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
