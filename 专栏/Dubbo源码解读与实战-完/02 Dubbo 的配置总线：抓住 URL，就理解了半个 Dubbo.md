<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>02 Dubbo 的配置总线：抓住 URL，就理解了半个 Dubbo.md</title>
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

                    
                    <a href="01&#32;&#32;Dubbo&#32;源码环境搭建：千里之行，始于足下.md">01  Dubbo 源码环境搭建：千里之行，始于足下.md</a>

                </li>
                <li>

                    <a class="current-tab" href="02&#32;Dubbo&#32;的配置总线：抓住&#32;URL，就理解了半个&#32;Dubbo.md">02 Dubbo 的配置总线：抓住 URL，就理解了半个 Dubbo.md</a>
                    

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
                        <div><h1>02 Dubbo 的配置总线：抓住 URL，就理解了半个 Dubbo</h1>
<p>你好，我是杨四正，今天我和你分享的主题是 Dubbo 的配置总线：抓住 URL，就理解了半个 Dubbo 。</p>
<p>在互联网领域，每个信息资源都有统一的且在网上唯一的地址，该地址就叫 URL（Uniform Resource Locator，统一资源定位符），它是互联网的统一资源定位标志，也就是指网络地址。</p>
<p>URL 本质上就是一个特殊格式的字符串。一个标准的 URL 格式可以包含如下的几个部分：</p>
<pre><code>protocol://username:<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="e999889a9a9e869b8da981869a9d">[email&#160;protected]</a>:port/path?key=value&amp;key=value
</code></pre>
<ul>
<li><strong>protocol</strong>：URL 的协议。我们常见的就是 HTTP 协议和 HTTPS 协议，当然，还有其他协议，如 FTP 协议、SMTP 协议等。</li>
<li><strong>username/password</strong>：用户名/密码。 HTTP Basic Authentication 中多会使用在 URL 的协议之后直接携带用户名和密码的方式。</li>
<li><strong>host/port</strong>：主机/端口。在实践中一般会使用域名，而不是使用具体的 host 和 port。</li>
<li><strong>path</strong>：请求的路径。</li>
<li><strong>parameters</strong>：参数键值对。一般在 GET 请求中会将参数放到 URL 中，POST 请求会将参数放到请求体中。</li>
</ul>
<p>URL 是整个 Dubbo 中非常基础，也是非常核心的一个组件，阅读源码的过程中你会发现很多方法都是以 URL 作为参数的，在方法内部解析传入的 URL 得到有用的参数，所以有人将 URL 称为<strong>Dubbo 的配置总线</strong>。</p>
<p>例如，在下一课时介绍的 Dubbo SPI 核心实现中，你会看到 URL 参与了扩展实现的确定；在本课程后续介绍注册中心实现的时候，你还会看到 Provider 将自身的信息封装成 URL 注册到 ZooKeeper 中，从而暴露自己的服务， Consumer 也是通过 URL 来确定自己订阅了哪些 Provider 的。</p>
<p>由此可见，URL 之于 Dubbo 是非常重要的，所以说“抓住 URL，就理解了半个 Dubbo”。那本文我们就来介绍 URL 在 Dubbo 中的应用，以及 URL 作为 Dubbo 统一契约的重要性，最后我们再通过示例说明 URL 在 Dubbo 中的具体应用。</p>
<h3>Dubbo 中的 URL</h3>
<p>Dubbo 中任意的一个实现都可以抽象为一个 URL，Dubbo 使用 URL 来统一描述了所有对象和配置信息，并贯穿在整个 Dubbo 框架之中。这里我们来看 Dubbo 中一个典型 URL 的示例，如下：</p>
<pre><code>dubbo://172.17.32.91:20880/org.apache.dubbo.demo.DemoService?anyhost=true&amp;application=dubbo-demo-api-provider&amp;dubbo=2.0.2&amp;interface=org.apache.dubbo.demo.DemoService&amp;methods=sayHello,sayHelloAsync&amp;pid=32508&amp;release=&amp;side=provider&amp;timestamp=1593253404714dubbo://172.17.32.91:20880/org.apache.dubbo.demo.DemoService?anyhost=true&amp;application=dubbo-demo-api-provider&amp;dubbo=2.0.2&amp;interface=org.apache.dubbo.demo.DemoService&amp;methods=sayHello,sayHelloAsync&amp;pid=32508&amp;release=&amp;side=provider&amp;timestamp=1593253404714
</code></pre>
<p>这个 Demo Provider 注册到 ZooKeeper 上的 URL 信息，简单解析一下这个 URL 的各个部分：</p>
<ul>
<li><strong>protocol</strong>：dubbo 协议。</li>
<li><strong>username/password</strong>：没有用户名和密码。</li>
<li><strong>host/port</strong>：172.17.32.91:20880。</li>
<li><strong>path</strong>：org.apache.dubbo.demo.DemoService。</li>
<li><strong>parameters</strong>：参数键值对，这里是问号后面的参数。</li>
</ul>
<p>下面是 URL 的构造方法，你可以看到其核心字段与前文分析的 URL 基本一致：</p>
<pre><code>public URL(String protocol, 

            String username, 

            String password, 

            String host, 

            int port, 

            String path, 

            Map&lt;String, String&gt; parameters, 

            Map&lt;String, Map&lt;String, String&gt;&gt; methodParameters) { 

    if (StringUtils.isEmpty(username) 

            &amp;&amp; StringUtils.isNotEmpty(password)) { 

        throw new IllegalArgumentException(&quot;Invalid url&quot;); 

    } 

    this.protocol = protocol; 

    this.username = username; 

    this.password = password; 

    this.host = host; 

    this.port = Math.max(port, 0); 

    this.address = getAddress(this.host, this.port); 

    while (path != null &amp;&amp; path.startsWith(&quot;/&quot;)) { 

        path = path.substring(1); 

    } 

    this.path = path; 

    if (parameters == null) { 

        parameters = new HashMap&lt;&gt;(); 

    } else { 

        parameters = new HashMap&lt;&gt;(parameters); 

    } 

    this.parameters = Collections.unmodifiableMap(parameters); 

    this.methodParameters = Collections.unmodifiableMap(methodParameters); 

}
</code></pre>
<p>另外，在 dubbo-common 包中还提供了 URL 的辅助类：</p>
<ul>
<li><strong>URLBuilder，</strong> 辅助构造 URL；</li>
<li><strong>URLStrParser，</strong> 将字符串解析成 URL 对象。</li>
</ul>
<h3>契约的力量</h3>
<p>对于 Dubbo 中的 URL，很多人称之为“配置总线”，也有人称之为“统一配置模型”。虽然说法不同，但都是在表达一个意思，URL 在 Dubbo 中被当作是“<strong>公共的契约</strong>”。一个 URL 可以包含非常多的扩展点参数，URL 作为上下文信息贯穿整个扩展点设计体系。</p>
<p>其实，一个优秀的开源产品都有一套灵活清晰的扩展契约，不仅是第三方可以按照这个契约进行扩展，其自身的内核也可以按照这个契约进行搭建。如果没有一个公共的契约，只是针对每个接口或方法进行约定，就会导致不同的接口甚至同一接口中的不同方法，以不同的参数类型进行传参，一会儿传递 Map，一会儿传递字符串，而且字符串的格式也不确定，需要你自己进行解析，这就多了一层没有明确表现出来的隐含的约定。</p>
<p>所以说，在 Dubbo 中使用 URL 的好处多多，增加了便捷性：</p>
<ul>
<li>使用 URL 这种公共契约进行上下文信息传递，最重要的就是代码更加易读、易懂，不用花大量时间去揣测传递数据的格式和含义，进而形成一个统一的规范，使得代码易写、易读。</li>
<li>使用 URL 作为方法的入参（相当于一个 Key/Value 都是 String 的 Map)，它所表达的含义比单个参数更丰富，当代码需要扩展的时候，可以将新的参数以 Key/Value 的形式追加到 URL 之中，而不需要改变入参或是返回值的结构。</li>
<li>使用 URL 这种“公共的契约”可以简化沟通，人与人之间的沟通消耗是非常大的，信息传递的效率非常低，使用统一的契约、术语、词汇范围，可以省去很多沟通成本，尽可能地提高沟通效率。</li>
</ul>
<h3>Dubbo 中的 URL 示例</h3>
<p>了解了 URL 的结构以及 Dubbo 使用 URL 的原因之后，我们再来看 Dubbo 中的三个真实示例，进一步感受 URL 的重要性。</p>
<h4>1. URL 在 SPI 中的应用</h4>
<p>Dubbo SPI 中有一个依赖 URL 的重要场景——适配器方法，是被 @Adaptive 注解标注的， URL 一个很重要的作用就是与 @Adaptive 注解一起选择合适的扩展实现类。</p>
<p>例如，在 dubbo-registry-api 模块中我们可以看到 RegistryFactory 这个接口，其中的 getRegistry() 方法上有 @Adaptive({&quot;protocol&quot;}) 注解，说明这是一个适配器方法，Dubbo 在运行时会为其动态生成相应的 “$Adaptive” 类型，如下所示：</p>
<pre><code>public class RegistryFactory$Adaptive

              implements RegistryFactory { 

    public Registry getRegistry(org.apache.dubbo.common.URL arg0) { 

        if (arg0 == null) throw new IllegalArgumentException(&quot;...&quot;); 

        org.apache.dubbo.common.URL url = arg0; 

        // 尝试获取URL的Protocol，如果Protocol为空，则使用默认值&quot;dubbo&quot; 

        String extName = (url.getProtocol() == null ? &quot;dubbo&quot; : 

             url.getProtocol()); 

        if (extName == null) 

            throw new IllegalStateException(&quot;...&quot;); 

        // 根据扩展名选择相应的扩展实现，Dubbo SPI的核心原理在下一课时深入分析 

        RegistryFactory extension = (RegistryFactory) ExtensionLoader 

          .getExtensionLoader(RegistryFactory.class) 

                .getExtension(extName); 

        return extension.getRegistry(arg0); 

    } 

}
</code></pre>
<p>我们会看到，在生成的 RegistryFactory$Adaptive 类中会自动实现 getRegistry() 方法，其中会根据 URL 的 Protocol 确定扩展名称，从而确定使用的具体扩展实现类。我们可以找到 RegistryProtocol 这个类，并在其 getRegistry() 方法中打一个断点， Debug 启动上一课时介绍的任意一个 Demo 示例中的 Provider，得到如下图所示的内容：</p>
<p><img src="assets/Ciqc1F8j2R2AO15wAAGHCEMA4ig361.png" alt="Drawing 0.png" /></p>
<p>这里传入的 registryUrl 值为：</p>
<pre><code>zookeeper://127.0.0.1:2181/org.apache.dubbo...
</code></pre>
<p>那么在 RegistryFactory$Adaptive 中得到的扩展名称为 zookeeper，此次使用的 Registry 扩展实现类就是 ZookeeperRegistryFactory。至于 Dubbo SPI 的完整内容，我们将在下一课时详细介绍，这里就不再展开了。</p>
<h4>2. URL 在服务暴露中的应用</h4>
<p>我们再来看另一个与 URL 相关的示例。上一课时我们在介绍 Dubbo 的简化架构时提到，Provider 在启动时，会将自身暴露的服务注册到 ZooKeeper 上，具体是注册哪些信息到 ZooKeeper 上呢？我们来看 ZookeeperRegistry.doRegister() 方法，在其中打个断点，然后 Debug 启动 Provider，会得到下图：</p>
<p><img src="assets/Ciqc1F8j2aGAJmTVAAI-2XB7V7o382.png" alt="Drawing 1.png" /></p>
<p>传入的 URL 中包含了 Provider 的地址（172.18.112.15:20880）、暴露的接口（org.apache.dubbo.demo.DemoService）等信息， toUrlPath() 方法会根据传入的 URL 参数确定在 ZooKeeper 上创建的节点路径，还会通过 URL 中的 dynamic 参数值确定创建的 ZNode 是临时节点还是持久节点。</p>
<h4>3. URL 在服务订阅中的应用</h4>
<p>Consumer 启动后会向注册中心进行订阅操作，并监听自己关注的 Provider。那 Consumer 是如何告诉注册中心自己关注哪些 Provider 呢？</p>
<p>我们来看 ZookeeperRegistry 这个实现类，它是由上面的 ZookeeperRegistryFactory 工厂类创建的 Registry 接口实现，其中的 doSubscribe() 方法是订阅操作的核心实现，在第 175 行打一个断点，并 Debug 启动 Demo 中 Consumer，会得到下图所示的内容：</p>
<p><img src="assets/CgqCHl8j822Aa3VpAAPpUoCBlf4288.png" alt="Lark20200731-183202.png" /></p>
<p>我们看到传入的 URL 参数如下：</p>
<pre><code>consumer://...?application=dubbo-demo-api-consumer&amp;category=providers,configurators,routers&amp;interface=org.apache.dubbo.demo.DemoService...
</code></pre>
<p>其中 Protocol 为 consumer ，表示是 Consumer 的订阅协议，其中的 category 参数表示要订阅的分类，这里要订阅 providers、configurators 以及 routers 三个分类；interface 参数表示订阅哪个服务接口，这里要订阅的是暴露 org.apache.dubbo.demo.DemoService 实现的 Provider。</p>
<p>通过 URL 中的上述参数，ZookeeperRegistry 会在 toCategoriesPath() 方法中将其整理成一个 ZooKeeper 路径，然后调用 zkClient 在其上添加监听。</p>
<p>通过上述示例，相信你已经感觉到 URL 在 Dubbo 体系中称为“总线”或是“契约”的原因了，在后面的源码分析中，我们还将看到更多关于 URL 的实现。</p>
<h3>总结</h3>
<p>在本课时，我们重点介绍了 Dubbo 对 URL 的封装以及相关的工具类，然后说明了统一契约的好处，当然也是 Dubbo 使用 URL 作为统一配置总线的好处，最后我们还介绍了 Dubbo SPI、Provider 注册、Consumer 订阅等场景中与 URL 相关的实现，这些都可以帮助你更好地感受 URL 在其中发挥的作用。</p>
<p>这里你可以想一下，在其他框架或是实际工作中，有没有类似 Dubbo URL 这种统一的契约？欢迎你在留言区分享你的想法。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="01&#32;&#32;Dubbo&#32;源码环境搭建：千里之行，始于足下.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="03&#32;&#32;Dubbo&#32;SPI&#32;精析，接口实现两极反转（上）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433ee1097870ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
