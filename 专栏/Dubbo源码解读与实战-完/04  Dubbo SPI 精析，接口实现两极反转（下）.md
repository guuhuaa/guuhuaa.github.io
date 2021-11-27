<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>04  Dubbo SPI 精析，接口实现两极反转（下）.md</title>
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

                    
                    <a href="02&#32;Dubbo&#32;的配置总线：抓住&#32;URL，就理解了半个&#32;Dubbo.md">02 Dubbo 的配置总线：抓住 URL，就理解了半个 Dubbo.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;Dubbo&#32;SPI&#32;精析，接口实现两极反转（上）.md">03  Dubbo SPI 精析，接口实现两极反转（上）.md</a>

                </li>
                <li>

                    <a class="current-tab" href="04&#32;&#32;Dubbo&#32;SPI&#32;精析，接口实现两极反转（下）.md">04  Dubbo SPI 精析，接口实现两极反转（下）.md</a>
                    

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
                        <div><h1>04  Dubbo SPI 精析，接口实现两极反转（下）</h1>
<p>在上一课时，我们一起学习了 JDK SPI 的基础使用以及核心原理，不过 Dubbo 并没有直接使用 JDK SPI 机制，而是借鉴其思想，实现了自身的一套 SPI 机制，这就是本课时将重点介绍的内容。</p>
<h3>Dubbo SPI</h3>
<p>在开始介绍 Dubbo SPI 实现之前，我们先来统一下面两个概念。</p>
<ul>
<li><strong>扩展点</strong>：通过 SPI 机制查找并加载实现的接口（又称“扩展接口”）。前文示例中介绍的 Log 接口、com.mysql.cj.jdbc.Driver 接口，都是扩展点。</li>
<li><strong>扩展点实现</strong>：实现了扩展接口的实现类。</li>
</ul>
<p>通过前面的分析可以发现，JDK SPI 在查找扩展实现类的过程中，需要遍历 SPI 配置文件中定义的所有实现类，该过程中会将这些实现类全部实例化。如果 SPI 配置文件中定义了多个实现类，而我们只需要使用其中一个实现类时，就会生成不必要的对象。例如，org.apache.dubbo.rpc.Protocol 接口有 InjvmProtocol、DubboProtocol、RmiProtocol、HttpProtocol、HessianProtocol、ThriftProtocol 等多个实现，如果使用 JDK SPI，就会加载全部实现类，导致资源的浪费。</p>
<p><strong>Dubbo SPI 不仅解决了上述资源浪费的问题，还对 SPI 配置文件扩展和修改。</strong></p>
<p>首先，Dubbo 按照 SPI 配置文件的用途，将其分成了三类目录。</p>
<ul>
<li>META-INF/services/ 目录：该目录下的 SPI 配置文件用来兼容 JDK SPI 。</li>
<li>META-INF/dubbo/ 目录：该目录用于存放用户自定义 SPI 配置文件。</li>
<li>META-INF/dubbo/internal/ 目录：该目录用于存放 Dubbo 内部使用的 SPI 配置文件。</li>
</ul>
<p>然后，Dubbo 将 SPI 配置文件改成了 <strong>KV 格式</strong>，例如：</p>
<pre><code>dubbo=org.apache.dubbo.rpc.protocol.dubbo.DubboProtocol
</code></pre>
<p>其中 key 被称为扩展名（也就是 ExtensionName），当我们在为一个接口查找具体实现类时，可以指定扩展名来选择相应的扩展实现。例如，这里指定扩展名为 dubbo，Dubbo SPI 就知道我们要使用：org.apache.dubbo.rpc.protocol.dubbo.DubboProtocol 这个扩展实现类，只实例化这一个扩展实现即可，无须实例化 SPI 配置文件中的其他扩展实现类。</p>
<p>使用 KV 格式的 SPI 配置文件的另一个好处是：让我们更容易定位到问题。假设我们使用的一个扩展实现类所在的 jar 包没有引入到项目中，那么 Dubbo SPI 在抛出异常的时候，会携带该扩展名信息，而不是简单地提示扩展实现类无法加载。这些更加准确的异常信息降低了排查问题的难度，提高了排查问题的效率。</p>
<p>下面我们正式进入 Dubbo SPI 核心实现的介绍。</p>
<h4>1. @SPI 注解</h4>
<p>Dubbo 中某个接口被 @SPI注解修饰时，就表示该接口是<strong>扩展接口</strong>，前文示例中的 org.apache.dubbo.rpc.Protocol 接口就是一个扩展接口：</p>
<p><img src="assets/CgqCHl8s936AYuePAABLd6cRz6w646.png" alt="Drawing 0.png" /></p>
<p>@SPI 注解的 value 值指定了默认的扩展名称，例如，在通过 Dubbo SPI 加载 Protocol 接口实现时，如果没有明确指定扩展名，则默认会将 @SPI 注解的 value 值作为扩展名，即加载 dubbo 这个扩展名对应的 org.apache.dubbo.rpc.protocol.dubbo.DubboProtocol 这个扩展实现类，相关的 SPI 配置文件在 dubbo-rpc-dubbo 模块中，如下图所示：</p>
<p><img src="assets/CgqCHl8s94mAaj2mAABcaXHNXqc467.png" alt="Drawing 1.png" /></p>
<p><strong>那 ExtensionLoader 是如何处理 @SPI 注解的呢？</strong></p>
<p>ExtensionLoader 位于 dubbo-common 模块中的 extension 包中，功能类似于 JDK SPI 中的 java.util.ServiceLoader。Dubbo SPI 的核心逻辑几乎都封装在 ExtensionLoader 之中（其中就包括 @SPI 注解的处理逻辑），其使用方式如下所示：</p>
<pre><code>Protocol protocol = ExtensionLoader 

   .getExtensionLoader(Protocol.class).getExtension(&quot;dubbo&quot;);
</code></pre>
<p>这里首先来了解一下 ExtensionLoader 中三个核心的静态字段。</p>
<ul>
<li><strong>strategies（LoadingStrategy[]类型）:</strong> LoadingStrategy 接口有三个实现（通过 JDK SPI 方式加载的），如下图所示，分别对应前面介绍的三个 Dubbo SPI 配置文件所在的目录，且都继承了 Prioritized 这个优先级接口，默认优先级是</li>
</ul>
<pre><code> DubboInternalLoadingStrategy &gt; DubboLoadingStrategy &gt; ServicesLoadingStrateg
</code></pre>
<p><img src="assets/Ciqc1F8s95mANXYKAADUVwBlgxs297.png" alt="Drawing 2.png" /></p>
<ul>
<li><strong>EXTENSION_LOADERS（ConcurrentMap&lt;Class, ExtensionLoader&gt;类型）</strong>
：Dubbo 中一个扩展接口对应一个 ExtensionLoader 实例，该集合缓存了全部 ExtensionLoader 实例，其中的 Key 为扩展接口，Value 为加载其扩展实现的 ExtensionLoader 实例。</li>
<li><strong>EXTENSION_INSTANCES（ConcurrentMap&lt;Class&lt;?&gt;, Object&gt;类型）</strong>：该集合缓存了扩展实现类与其实例对象的映射关系。在前文示例中，Key 为 Class，Value 为 DubboProtocol 对象。</li>
</ul>
<p>下面我们再来关注一下 ExtensionLoader 的实例字段。</p>
<ul>
<li><strong>type（Class&lt;?&gt;类型）</strong>：当前 ExtensionLoader 实例负责加载扩展接口。</li>
<li><strong>cachedDefaultName（String类型）</strong>：记录了 type 这个扩展接口上 @SPI 注解的 value 值，也就是默认扩展名。</li>
<li><strong>cachedNames（ConcurrentMap&lt;Class&lt;?&gt;, String&gt;类型）</strong>：缓存了该 ExtensionLoader 加载的扩展实现类与扩展名之间的映射关系。</li>
<li><strong>cachedClasses（Holder&lt;Map&lt;String, Class&lt;?&gt;&gt;&gt;类型）</strong>：缓存了该 ExtensionLoader 加载的扩展名与扩展实现类之间的映射关系。cachedNames 集合的反向关系缓存。</li>
<li><strong>cachedInstances（ConcurrentMap&lt;String, Holder<Object>&gt;类型）</strong>：缓存了该 ExtensionLoader 加载的扩展名与扩展实现对象之间的映射关系。</li>
</ul>
<p>ExtensionLoader.getExtensionLoader() 方法会根据扩展接口从 EXTENSION_LOADERS 缓存中查找相应的 ExtensionLoader 实例，核心实现如下：</p>
<pre><code>public static &lt;T&gt; ExtensionLoader&lt;T&gt; getExtensionLoader(Class&lt;T&gt; type) { 

    ExtensionLoader&lt;T&gt; loader =

         (ExtensionLoader&lt;T&gt;) EXTENSION_LOADERS.get(type); 

    if (loader == null) { 

        EXTENSION_LOADERS.putIfAbsent(type, 

               new ExtensionLoader&lt;T&gt;(type)); 

        loader = (ExtensionLoader&lt;T&gt;) EXTENSION_LOADERS.get(type); 

    } 

    return loader; 

}
</code></pre>
<p>得到接口对应的 ExtensionLoader 对象之后会调用其 getExtension() 方法，根据传入的扩展名称从 cachedInstances 缓存中查找扩展实现的实例，最终将其实例化后返回：</p>
<pre><code>public T getExtension(String name) { 

    // getOrCreateHolder()方法中封装了查找cachedInstances缓存的逻辑 

    Holder&lt;Object&gt; holder = getOrCreateHolder(name); 

    Object instance = holder.get(); 

    if (instance == null) { // double-check防止并发问题 

        synchronized (holder) { 

            instance = holder.get(); 

            if (instance == null) { 

                // 根据扩展名从SPI配置文件中查找对应的扩展实现类 

                instance = createExtension(name); 

                holder.set(instance); 

            } 

        } 

    } 

    return (T) instance; 

}
</code></pre>
<p>在 createExtension() 方法中完成了 SPI 配置文件的查找以及相应扩展实现类的实例化，同时还实现了自动装配以及自动 Wrapper 包装等功能。其核心流程是这样的：</p>
<ol>
<li>获取 cachedClasses 缓存，根据扩展名从 cachedClasses 缓存中获取扩展实现类。如果 cachedClasses 未初始化，则会扫描前面介绍的三个 SPI 目录获取查找相应的 SPI 配置文件，然后加载其中的扩展实现类，最后将扩展名和扩展实现类的映射关系记录到 cachedClasses 缓存中。这部分逻辑在 loadExtensionClasses() 和 loadDirectory() 方法中。</li>
<li>根据扩展实现类从 EXTENSION_INSTANCES 缓存中查找相应的实例。如果查找失败，会通过反射创建扩展实现对象。</li>
<li><strong>自动装配</strong>扩展实现对象中的属性（即调用其 setter）。这里涉及 ExtensionFactory 以及自动装配的相关内容，本课时后面会进行详细介绍。</li>
<li><strong>自动包装</strong>扩展实现对象。这里涉及 Wrapper 类以及自动包装特性的相关内容，本课时后面会进行详细介绍。</li>
<li>如果扩展实现类实现了 Lifecycle 接口，在 initExtension() 方法中会调用 initialize() 方法进行初始化。</li>
</ol>
<pre><code>private T createExtension(String name) { 

    Class&lt;?&gt; clazz = getExtensionClasses().get(name); // --- 1 

    if (clazz == null) { 

        throw findException(name); 

    } 

    try { 

        T instance = (T) EXTENSION_INSTANCES.get(clazz); // --- 2 

        if (instance == null) { 

            EXTENSION_INSTANCES.putIfAbsent(clazz, clazz.newInstance()); 

            instance = (T) EXTENSION_INSTANCES.get(clazz); 

        } 

        injectExtension(instance); // --- 3 

        Set&lt;Class&lt;?&gt;&gt; wrapperClasses = cachedWrapperClasses; // --- 4 

        if (CollectionUtils.isNotEmpty(wrapperClasses)) { 

            for (Class&lt;?&gt; wrapperClass : wrapperClasses) { 

                instance = injectExtension((T) wrapperClass.getConstructor(type).newInstance(instance)); 

            } 

        } 

        initExtension(instance); // ---5

        return instance; 

    } catch (Throwable t) { 

        throw new IllegalStateException(&quot;Extension instance (name: &quot; + name + &quot;, class: &quot; + 

                type + &quot;) couldn't be instantiated: &quot; + t.getMessage(), t); 

    } 

}
</code></pre>
<h4>2. @Adaptive 注解与适配器</h4>
<p>@Adaptive 注解用来实现 Dubbo 的适配器功能，那什么是适配器呢？这里我们通过一个示例进行说明。Dubbo 中的 ExtensionFactory 接口有三个实现类，如下图所示，ExtensionFactory 接口上有 @SPI 注解，AdaptiveExtensionFactory 实现类上有 @Adaptive 注解。</p>
<p><img src="assets/Ciqc1F8s-D6AZFtdAAC318rtQ-I710.png" alt="Drawing 3.png" /></p>
<p>AdaptiveExtensionFactory 不实现任何具体的功能，而是用来适配 ExtensionFactory 的 SpiExtensionFactory 和 SpringExtensionFactory 这两种实现。AdaptiveExtensionFactory 会根据运行时的一些状态来选择具体调用 ExtensionFactory 的哪个实现。</p>
<p>@Adaptive 注解还可以加到接口方法之上，Dubbo 会动态生成适配器类。例如，Transporter接口有两个被 @Adaptive 注解修饰的方法：</p>
<pre><code>@SPI(&quot;netty&quot;) 

public interface Transporter { 

    @Adaptive({Constants.SERVER_KEY, Constants.TRANSPORTER_KEY}) 

    RemotingServer bind(URL url, ChannelHandler handler) throws RemotingException; 

    @Adaptive({Constants.CLIENT_KEY, Constants.TRANSPORTER_KEY}) 

    Client connect(URL url, ChannelHandler handler) throws RemotingException; 

}
</code></pre>
<p>Dubbo 会生成一个 Transporter$Adaptive 适配器类，该类继承了 Transporter 接口：</p>
<pre><code>public class Transporter$Adaptive implements Transporter { 

    public org.apache.dubbo.remoting.Client connect(URL arg0, ChannelHandler arg1) throws RemotingException { 

        // 必须传递URL参数 

        if (arg0 == null) throw new IllegalArgumentException(&quot;url == null&quot;); 

        URL url = arg0; 

        // 确定扩展名，优先从URL中的client参数获取，其次是transporter参数 

        // 这两个参数名称由@Adaptive注解指定，最后是@SPI注解中的默认值 

        String extName = url.getParameter(&quot;client&quot;,

            url.getParameter(&quot;transporter&quot;, &quot;netty&quot;)); 

        if (extName == null) 

            throw new IllegalStateException(&quot;...&quot;); 

        // 通过ExtensionLoader加载Transporter接口的指定扩展实现 

        Transporter extension = (Transporter) ExtensionLoader 

              .getExtensionLoader(Transporter.class) 

                    .getExtension(extName); 

        return extension.connect(arg0, arg1); 

    } 

    ... // 省略bind()方法 

}
</code></pre>
<p>生成 Transporter$Adaptive 这个类的逻辑位于 ExtensionLoader.createAdaptiveExtensionClass() 方法，若感兴趣你可以看一下相关代码，其中涉及的 javassist 等方面的知识，在后面的课时中我们会进行介绍。</p>
<p>明确了 @Adaptive 注解的作用之后，我们回到 ExtensionLoader.createExtension() 方法，其中在扫描 SPI 配置文件的时候，会调用 loadClass() 方法加载 SPI 配置文件中指定的类，如下图所示：</p>
<p><img src="assets/CgqCHl8s-H2AJE1LAACILXqbtHY819.png" alt="Drawing 4.png" /></p>
<p>loadClass() 方法中会识别加载扩展实现类上的 @Adaptive 注解，将该扩展实现的类型缓存到 cachedAdaptiveClass 这个实例字段上（volatile修饰）：</p>
<pre><code>private void loadClass(){ 

    if (clazz.isAnnotationPresent(Adaptive.class)) { 

        // 缓存到cachedAdaptiveClass字段 

        cacheAdaptiveClass(clazz, overridden);

    } else ... // 省略其他分支 

}
</code></pre>
<p>我们可以通过 ExtensionLoader.getAdaptiveExtension() 方法获取适配器实例，并将该实例缓存到 cachedAdaptiveInstance 字段（Holder类型）中，核心流程如下：</p>
<ul>
<li>首先，检查 cachedAdaptiveInstance 字段中是否已缓存了适配器实例，如果已缓存，则直接返回该实例即可。</li>
<li>然后，调用 getExtensionClasses() 方法，其中就会触发前文介绍的 loadClass() 方法，完成 cachedAdaptiveClass 字段的填充。</li>
<li>如果存在 @Adaptive 注解修饰的扩展实现类，该类就是适配器类，通过 newInstance() 将其实例化即可。如果不存在 @Adaptive 注解修饰的扩展实现类，就需要通过 createAdaptiveExtensionClass() 方法扫描扩展接口中方法上的 @Adaptive 注解，动态生成适配器类，然后实例化。</li>
<li>接下来，调用 injectExtension() 方法进行自动装配，就能得到一个完整的适配器实例。</li>
<li>最后，将适配器实例缓存到 cachedAdaptiveInstance 字段，然后返回适配器实例。</li>
</ul>
<p>getAdaptiveExtension() 方法的流程涉及多个方法，这里不再粘贴代码，感兴趣的同学可以参考上述流程分析相应源码。</p>
<p>此外，我们还可以通过 API 方式（addExtension() 方法）设置 cachedAdaptiveClass 这个字段，指定适配器类型（这个方法你知道即可）。</p>
<p>总之，适配器什么实际工作都不用做，就是根据参数和状态选择其他实现来完成工作。 。</p>
<h4>3. 自动包装特性</h4>
<p>Dubbo 中的一个扩展接口可能有多个扩展实现类，这些扩展实现类可能会包含一些相同的逻辑，如果在每个实现类中都写一遍，那么这些重复代码就会变得很难维护。Dubbo 提供的自动包装特性，就可以解决这个问题。 Dubbo 将多个扩展实现类的公共逻辑，抽象到 Wrapper 类中，Wrapper 类与普通的扩展实现类一样，也实现了扩展接口，在获取真正的扩展实现对象时，在其外面包装一层 Wrapper 对象，你可以理解成一层装饰器。</p>
<p>了解了 Wrapper 类的基本功能，我们回到 ExtensionLoader.loadClass() 方法中，可以看到：</p>
<pre><code>private void loadClass(){ 

    ... // 省略前面对@Adaptive注解的处理 

    } else if (isWrapperClass(clazz)) { // ---1 

        cacheWrapperClass(clazz); // ---2 

    } else ... // 省略其他分支

}
</code></pre>
<ol>
<li>在 isWrapperClass() 方法中，会判断该扩展实现类是否包含拷贝构造函数（即构造函数只有一个参数且为扩展接口类型），如果包含，则为 Wrapper 类，这就是判断 Wrapper 类的标准。</li>
<li>将 Wrapper 类记录到 cachedWrapperClasses（Set&lt;Class&lt;?&gt;&gt;类型）这个实例字段中进行缓存。</li>
</ol>
<p>前面在介绍 createExtension() 方法时的 4 处，有下面这段代码，其中会遍历全部 Wrapper 类并一层层包装到真正的扩展实例对象外层：</p>
<pre><code>Set&lt;Class&lt;?&gt;&gt; wrapperClasses = cachedWrapperClasses;

if (CollectionUtils.isNotEmpty(wrapperClasses)) { 

    for (Class&lt;?&gt; wrapperClass : wrapperClasses) { 

        instance = injectExtension((T) wrapperClass 

            .getConstructor(type).newInstance(instance)); 

    } 

}
</code></pre>
<h4>4. 自动装配特性</h4>
<p>在 createExtension() 方法中我们看到，Dubbo SPI 在拿到扩展实现类的对象（以及 Wrapper 类的对象）之后，还会调用 injectExtension() 方法扫描其全部 setter 方法，并根据 setter 方法的名称以及参数的类型，加载相应的扩展实现，然后调用相应的 setter 方法填充属性，这就实现了 Dubbo SPI 的自动装配特性。简单来说，自动装配属性就是在加载一个扩展点的时候，将其依赖的扩展点一并加载，并进行装配。</p>
<p>下面简单看一下 injectExtension() 方法的具体实现：</p>
<pre><code>private T injectExtension(T instance) { 

    if (objectFactory == null) { // 检测objectFactory字段 

        return instance; 

    } 

    for (Method method : instance.getClass().getMethods()) { 

        ... // 如果不是setter方法，忽略该方法(略) 

        if (method.getAnnotation(DisableInject.class) != null) { 

            continue; // 如果方法上明确标注了@DisableInject注解，忽略该方法 

        } 

        // 根据setter方法的参数，确定扩展接口 

        Class&lt;?&gt; pt = method.getParameterTypes()[0]; 

        ... // 如果参数为简单类型，忽略该setter方法(略) 

        // 根据setter方法的名称确定属性名称 

        String property = getSetterProperty(method); 

        // 加载并实例化扩展实现类 

        Object object = objectFactory.getExtension(pt, property); 

        if (object != null) { 

            method.invoke(instance, object); // 调用setter方法进行装配 

        } 

    } 

    return instance; 

}
</code></pre>
<p>injectExtension() 方法实现的自动装配依赖了 ExtensionFactory（即 objectFactory 字段），前面我们提到过 ExtensionFactory 有 SpringExtensionFactory 和 SpiExtensionFactory 两个真正的实现（还有一个实现是 AdaptiveExtensionFactory 是适配器）。下面我们分别介绍下这两个真正的实现。</p>
<p><strong>第一个，SpiExtensionFactory。</strong> 根据扩展接口获取相应的适配器，没有到属性名称：</p>
<pre><code>@Override 

public &lt;T&gt; T getExtension(Class&lt;T&gt; type, String name) { 

    if (type.isInterface() &amp;&amp; type.isAnnotationPresent(SPI.class)) { 

        // 查找type对应的ExtensionLoader实例 

        ExtensionLoader&lt;T&gt; loader = ExtensionLoader 

          .getExtensionLoader(type); 

        if (!loader.getSupportedExtensions().isEmpty()) { 

            return loader.getAdaptiveExtension(); // 获取适配器实现 

        } 

    } 

    return null; 

}
</code></pre>
<p><strong>第二个，SpringExtensionFactory。</strong> 将属性名称作为 Spring Bean 的名称，从 Spring 容器中获取 Bean：</p>
<pre><code>public &lt;T&gt; T getExtension(Class&lt;T&gt; type, String name) { 

    ... // 检查:type必须为接口且必须包含@SPI注解(略) 

    for (ApplicationContext context : CONTEXTS) { 

        // 从Spring容器中查找Bean 

        T bean = BeanFactoryUtils.getOptionalBean(context,name,type); 

        if (bean != null) { 

            return bean; 

        } 

    } 

    return null; 

}
</code></pre>
<h4>5. @Activate注解与自动激活特性</h4>
<p>这里以 Dubbo 中的 Filter 为例说明自动激活特性的含义，org.apache.dubbo.rpc.Filter 接口有非常多的扩展实现类，在一个场景中可能需要某几个 Filter 扩展实现类协同工作，而另一个场景中可能需要另外几个实现类一起工作。这样，就需要一套配置来指定当前场景中哪些 Filter 实现是可用的，这就是 @Activate 注解要做的事情。</p>
<p>@Activate 注解标注在扩展实现类上，有 group、value 以及 order 三个属性。</p>
<ul>
<li>group 属性：修饰的实现类是在 Provider 端被激活还是在 Consumer 端被激活。</li>
<li>value 属性：修饰的实现类只在 URL 参数中出现指定的 key 时才会被激活。</li>
<li>order 属性：用来确定扩展实现类的排序。</li>
</ul>
<p>我们先来看 loadClass() 方法对 @Activate 的扫描，其中会将包含 @Activate 注解的实现类缓存到 cachedActivates 这个实例字段（Map&lt;String, Object&gt;类型，Key为扩展名，Value为 @Activate 注解）：</p>
<pre><code>private void loadClass(){ 

    if (clazz.isAnnotationPresent(Adaptive.class)) { 

        // 处理@Adaptive注解 

        cacheAdaptiveClass(clazz, overridden); 

    } else if (isWrapperClass(clazz)) { // 处理Wrapper类 

        cacheWrapperClass(clazz); 

    } else { // 处理真正的扩展实现类 

        clazz.getConstructor(); // 扩展实现类必须有无参构造函数 

        ...// 兜底:SPI配置文件中未指定扩展名称，则用类的简单名称作为扩展名(略) 

        String[] names = NAME_SEPARATOR.split(name); 

        if (ArrayUtils.isNotEmpty(names)) { 

            // 将包含@Activate注解的实现类缓存到cachedActivates集合中 

            cacheActivateClass(clazz, names[0]); 

            for (String n : names) { 

                // 在cachedNames集合中缓存实现类-&gt;扩展名的映射 

                cacheName(clazz, n);

                // 在cachedClasses集合中缓存扩展名-&gt;实现类的映射 

                saveInExtensionClass(extensionClasses, clazz, n, 

                     overridden); 

            } 

        } 

    } 

}
</code></pre>
<p>使用 cachedActivates 这个集合的地方是 getActivateExtension() 方法。首先来关注 getActivateExtension() 方法的参数：url 中包含了配置信息，values 是配置中指定的扩展名，group 为 Provider 或 Consumer。下面是 getActivateExtension() 方法的核心逻辑：</p>
<ol>
<li>首先，获取默认激活的扩展集合。默认激活的扩展实现类有几个条件：①在 cachedActivates 集合中存在；②@Activate 注解指定的 group 属性与当前 group 匹配；③扩展名没有出现在 values 中（即未在配置中明确指定，也未在配置中明确指定删除）；④URL 中出现了 @Activate 注解中指定的 Key。</li>
<li>然后，按照 @Activate 注解中的 order 属性对默认激活的扩展集合进行排序。</li>
<li>最后，按序添加自定义扩展实现类的对象。</li>
</ol>
<pre><code>public List&lt;T&gt; getActivateExtension(URL url, String[] values, 

         String group) { 

    List&lt;T&gt; activateExtensions = new ArrayList&lt;&gt;(); 

    // values配置就是扩展名 

    List&lt;String&gt; names = values == null ?

            new ArrayList&lt;&gt;(0) : asList(values); 

    if (!names.contains(REMOVE_VALUE_PREFIX + DEFAULT_KEY)) {// ---1 

        getExtensionClasses(); // 触发cachedActivates等缓存字段的加载 

        for (Map.Entry&lt;String, Object&gt; entry :

                  cachedActivates.entrySet()) { 

            String name = entry.getKey(); // 扩展名 

            Object activate = entry.getValue(); // @Activate注解 

            String[] activateGroup, activateValue; 

            if (activate instanceof Activate) { // @Activate注解中的配置 

                activateGroup = ((Activate) activate).group(); 

                activateValue = ((Activate) activate).value(); 

            } else { 

                continue; 

            } 

            if (isMatchGroup(group, activateGroup) // 匹配group 

                    // 没有出现在values配置中的，即为默认激活的扩展实现 

                    &amp;&amp; !names.contains(name)

                    // 通过&quot;-&quot;明确指定不激活该扩展实现 

                    &amp;&amp; !names.contains(REMOVE_VALUE_PREFIX + name)

                    // 检测URL中是否出现了指定的Key 

                    &amp;&amp; isActive(activateValue, url)) { 

                // 加载扩展实现的实例对象，这些都是激活的 

                activateExtensions.add(getExtension(name)); 

            } 

        } 

        // 排序 --- 2 

        activateExtensions.sort(ActivateComparator.COMPARATOR); 

    } 

    List&lt;T&gt; loadedExtensions = new ArrayList&lt;&gt;(); 

    for (int i = 0; i &lt; names.size(); i++) { // ---3 

        String name = names.get(i); 

        // 通过&quot;-&quot;开头的配置明确指定不激活的扩展实现，直接就忽略了 

        if (!name.startsWith(REMOVE_VALUE_PREFIX) 

                &amp;&amp; !names.contains(REMOVE_VALUE_PREFIX + name)) { 

            if (DEFAULT_KEY.equals(name)) { 

                if (!loadedExtensions.isEmpty()) { 

                    // 按照顺序，将自定义的扩展添加到默认扩展集合前面 

                    activateExtensions.addAll(0, loadedExtensions); 

                    loadedExtensions.clear(); 

                } 

            } else { 

                loadedExtensions.add(getExtension(name)); 

            } 

        } 

    } 

    if (!loadedExtensions.isEmpty()) { 

        // 按照顺序，将自定义的扩展添加到默认扩展集合后面 

        activateExtensions.addAll(loadedExtensions); 

    } 

    return activateExtensions; 

}
</code></pre>
<p>最后举个简单的例子说明上述处理流程，假设 cachedActivates 集合缓存的扩展实现如下表所示：</p>
<p><img src="assets/CgqCHl8tNGCAIw8fAACXC_dle_g809.png" alt="11.png" /></p>
<p>在 Provider 端调用 getActivateExtension() 方法时传入的 values 配置为 &quot;demoFilter3、-demoFilter2、default、demoFilter1&quot;，那么根据上面的逻辑：</p>
<ol>
<li>得到默认激活的扩展实实现集合中有 [ demoFilter4, demoFilter6 ]；</li>
<li>排序后为 [ demoFilter6, demoFilter4 ]；</li>
<li>按序添加自定义扩展实例之后得到 [ demoFilter3, demoFilter6, demoFilter4, demoFilter1 ]。</li>
</ol>
<h3>总结</h3>
<p>本课时我们深入全面地讲解了 Dubbo SPI 的核心实现：首先介绍了 @SPI 注解的底层实现，这是 Dubbo SPI 最核心的基础；然后介绍了 @Adaptive 注解与动态生成适配器类的核心原理和实现；最后分析了 Dubbo SPI 中的自动包装和自动装配特性，以及 @Activate 注解的原理。</p>
<p>Dubbo SPI 是 Dubbo 框架实现扩展机制的核心，希望你仔细研究其实现，为后续源码分析过程打下基础。</p>
<p>也欢迎你在留言区分享你的学习心得和实践经验。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="03&#32;&#32;Dubbo&#32;SPI&#32;精析，接口实现两极反转（上）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="05&#32;&#32;海量定时任务，一个时间轮搞定.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433eeec85170ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
