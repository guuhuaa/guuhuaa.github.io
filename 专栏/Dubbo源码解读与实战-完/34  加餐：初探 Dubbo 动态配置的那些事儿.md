<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>34  加餐：初探 Dubbo 动态配置的那些事儿.md</title>
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

                    <a class="current-tab" href="34&#32;&#32;加餐：初探&#32;Dubbo&#32;动态配置的那些事儿.md">34  加餐：初探 Dubbo 动态配置的那些事儿.md</a>
                    

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
                        <div><h1>34  加餐：初探 Dubbo 动态配置的那些事儿</h1>
<p>在前面第 31 课时中我们详细讲解了 RegistryDirectory 相关的内容，作为一个 NotifyListener 监听器，RegistryDirectory 会同时监听注册中心的 providers、routers 和 configurators 三个目录。通过 RegistryDirectory 处理 configurators 目录的逻辑，我们了解到 configurators 目录中动态添加的 URL 会覆盖 providers 目录下注册的 Provider URL，Dubbo 还会按照 configurators 目录下的最新配置，重新创建 Invoker 对象（同时会销毁原来的 Invoker 对象）。</p>
<p>在老版本的 Dubbo 中，我们可以通过服务治理控制台向注册中心的 configurators 目录写入动态配置的 URL。在 Dubbo 2.7.x 版本中，动态配置信息除了可以写入注册中心的 configurators 目录之外，还可以写入外部的配置中心，这部分内容我们将在后面的课时详细介绍，今天这一课时我们重点来看<strong>写入注册中心的动态配置。</strong></p>
<p>首先，我们需要了解一下 configurators 目录中 URL 都有哪些协议以及这些协议的含义，然后还要知道 Dubbo 是如何解析这些 URL 得到 Configurator 对象的，以及 Configurator 是如何与已有的 Provider URL 共同作用得到实现动态更新配置的效果。</p>
<h3>基础协议</h3>
<p>首先，我们需要了解<strong>写入注册中心 configurators 中的动态配置有 override 和 absent 两种协议</strong>。下面是一个 override 协议的示例：</p>
<pre><code>override://0.0.0.0/org.apache.dubbo.demo.DemoService?category=configurators&amp;dynamic=false&amp;enabled=true&amp;application=dubbo-demo-api-consumer&amp;timeout=1000
</code></pre>
<p>那这个 URL 中各个部分的含义是怎样的呢？下面我们就一个一个来分析下。</p>
<ul>
<li>override，表示采用覆盖方式。Dubbo 支持 override 和 absent 两种协议，我们也可以通过 SPI 的方式进行扩展。</li>
<li>0.0.0.0，表示对所有 IP 生效。如果只想覆盖某个特定 IP 的 Provider 配置，可以使用该 Provider 的具体 IP。</li>
<li>org.apache.dubbo.demo.DemoService，表示只对指定服务生效。</li>
<li>category=configurators，表示该 URL 为动态配置类型。</li>
<li>dynamic=false，表示该 URL 为持久数据，即使注册该 URL 的节点退出，该 URL 依旧会保存在注册中心。</li>
<li>enabled=true，表示该 URL 的覆盖规则已生效。</li>
<li>application=dubbo-demo-api-consumer，表示只对指定应用生效。如果不指定，则默认表示对所有应用都生效。</li>
<li>timeout=1000，表示将满足以上条件 Provider URL 中的 timeout 参数值覆盖为 1000。如果想覆盖其他配置，可以直接以参数的形式添加到 override URL 之上。</li>
</ul>
<p>在 Dubbo 的官网中，还提供了一些简单示例，我们这里也简单解读一下。</p>
<ul>
<li>禁用某个 Provider，通常用于临时剔除某个 Provider 节点：</li>
</ul>
<pre><code>override://10.20.153.10/com.foo.BarService?category=configurators&amp;dynamic=false&amp;disabled=true
</code></pre>
<ul>
<li>调整某个 Provider 的权重为 200：</li>
</ul>
<pre><code>override://10.20.153.10/com.foo.BarService?category=configurators&amp;dynamic=false&amp;weight=200
</code></pre>
<ul>
<li>调整负载均衡策略为 LeastActiveLoadBalance（负载均衡的内容会在下一课时详细介绍）：</li>
</ul>
<pre><code>override://10.20.153.10/com.foo.BarService?category=configurators&amp;dynamic=false&amp;loadbalance=leastactive
</code></pre>
<ul>
<li>服务降级，通常用于临时屏蔽某个出错的非关键服务（mock 机制的具体实现我们会在后面的课时详细介绍）：</li>
</ul>
<pre><code>override://0.0.0.0/com.foo.BarService?category=configurators&amp;dynamic=false&amp;application=foo&amp;mock=force:return+null
</code></pre>
<h3>Configurator</h3>
<p>当我们在注册中心的 configurators 目录中添加 override（或 absent）协议的 URL 时，Registry 会收到注册中心的通知，回调注册在其上的 NotifyListener，其中就包括 RegistryDirectory。我们在第 31 课时中已经详细分析了 RegistryDirectory.notify() 处理 providers、configurators 和 routers 目录变更的流程，其中 configurators 目录下 URL 会被解析成 Configurator 对象。</p>
<p>Configurator 接口抽象了一条配置信息，同时提供了将配置 URL 解析成 Configurator 对象的工具方法。Configurator 接口具体定义如下：</p>
<pre><code>public interface Configurator extends Comparable&lt;Configurator&gt; {

    // 获取该Configurator对象对应的配置URL，例如前文介绍的override协议URL

    URL getUrl();

    // configure()方法接收的参数是原始URL，返回经过Configurator修改后的URL

    URL configure(URL url);

    // toConfigurators()工具方法可以将多个配置URL对象解析成相应的Configurator对象

    static Optional&lt;List&lt;Configurator&gt;&gt; toConfigurators(List&lt;URL&gt; urls) {

        // 创建ConfiguratorFactory适配器

        ConfiguratorFactory configuratorFactory = ExtensionLoader.getExtensionLoader(ConfiguratorFactory.class)

                .getAdaptiveExtension();

        List&lt;Configurator&gt; configurators = new ArrayList&lt;&gt;(urls.size()); // 记录解析的结果

        for (URL url : urls) {

            // 遇到empty协议，直接清空configurators集合，结束解析，返回空集合

            if (EMPTY_PROTOCOL.equals(url.getProtocol())) {

                configurators.clear();

                break;

            }

            Map&lt;String, String&gt; override = new HashMap&lt;&gt;(url.getParameters());

            override.remove(ANYHOST_KEY);

            if (override.size() == 0) { // 如果该配置URL没有携带任何参数，则跳过该URL

                configurators.clear();

                continue;

            }

            // 通过ConfiguratorFactory适配器选择合适ConfiguratorFactory扩展，并创建Configurator对象

          configurators.add(configuratorFactory.getConfigurator(url));

        }

        Collections.sort(configurators); // 排序

        return Optional.of(configurators);

    }

    // 排序首先按照ip进行排序，所有ip的优先级都高于0.0.0.0，当ip相同时，会按照priority参数值进行排序

    default int compareTo(Configurator o) {

        if (o == null) {

            return -1;

        }

        int ipCompare = getUrl().getHost().compareTo(o.getUrl().getHost());

        if (ipCompare == 0) {

            int i = getUrl().getParameter(PRIORITY_KEY, 0);

            int j = o.getUrl().getParameter(PRIORITY_KEY, 0);

            return Integer.compare(i, j);

        } else {

            return ipCompare;

        }

    }
</code></pre>
<p>ConfiguratorFactory 接口是一个扩展接口，Dubbo 提供了两个实现类，如下图所示：</p>
<p><img src="assets/CgqCHl-3eLqAL0VKAAGW_mZ-1yE800.png" alt="Lark20201120-160501.png" /></p>
<p>ConfiguratorFactory 继承关系图</p>
<p>其中，OverrideConfiguratorFactory 对应的扩展名为 override，创建的 Configurator 实现是 OverrideConfigurator；AbsentConfiguratorFactory 对应的扩展名是 absent，创建的 Configurator 实现类是 AbsentConfigurator。</p>
<p>Configurator 接口的继承关系如下图所示：</p>
<p><img src="assets/Ciqc1F-3eMCAP6pVAAGo31X0Wd8652.png" alt="Lark20201120-160505.png" /></p>
<p>Configurator 继承关系图</p>
<p>其中，AbstractConfigurator 中维护了一个 configuratorUrl 字段，记录了完整的配置 URL。<strong>AbstractConfigurator 是一个模板类，其核心实现是 configure() 方法</strong>，具体实现如下：</p>
<pre><code>public URL configure(URL url) {

    // 这里会根据配置URL的enabled参数以及host决定该URL是否可用，同时还会根据原始URL是否为空以及原始URL的host是否为空，决定当前是否执行后续覆盖逻辑

    if (!configuratorUrl.getParameter(ENABLED_KEY, true) || configuratorUrl.getHost() == null || url == null || url.getHost() == null) {

        return url;

    }

    // 针对2.7.0之后版本，这里添加了一个configVersion参数作为区分

    String apiVersion = configuratorUrl.getParameter(CONFIG_VERSION_KEY);

    if (StringUtils.isNotEmpty(apiVersion)) { // 对2.7.0之后版本的配置处理

        String currentSide = url.getParameter(SIDE_KEY);

        String configuratorSide = configuratorUrl.getParameter(SIDE_KEY);

        // 根据配置URL中的side参数以及原始URL中的side参数值进行匹配

        if (currentSide.equals(configuratorSide) &amp;&amp; CONSUMER.equals(configuratorSide) &amp;&amp; 0 == configuratorUrl.getPort()) {

            url = configureIfMatch(NetUtils.getLocalHost(), url);

        } else if (currentSide.equals(configuratorSide) &amp;&amp; PROVIDER.equals(configuratorSide) &amp;&amp; url.getPort() == configuratorUrl.getPort()) {

            url = configureIfMatch(url.getHost(), url);

        }

    } else { // 2.7.0版本之前对配置的处理

        url = configureDeprecated(url);

    }

    return url;

}
</code></pre>
<p>这里我们需要关注下<strong>configureDeprecated() 方法对历史版本的兼容</strong>，其实这也是对注册中心 configurators 目录下配置 URL 的处理，具体实现如下：</p>
<pre><code>private URL configureDeprecated(URL url) {

    // 如果配置URL中的端口不为空，则是针对Provider的，需要判断原始URL的端口，两者端口相同，才能执行configureIfMatch()方法中的配置方法

    if (configuratorUrl.getPort() != 0) {

        if (url.getPort() == configuratorUrl.getPort()) {

            return configureIfMatch(url.getHost(), url);

        }

    } else {

        // 如果没有指定端口，则该配置URL要么是针对Consumer的，要么是针对任意URL的（即host为0.0.0.0）

        // 如果原始URL属于Consumer，则使用Consumer的host进行匹配

        if (url.getParameter(SIDE_KEY, PROVIDER).equals(CONSUMER)) {

            return configureIfMatch(NetUtils.getLocalHost(), url);

        } else if (url.getParameter(SIDE_KEY, CONSUMER).equals(PROVIDER)) {

            // 如果是Provider URL，则用0.0.0.0来配置

            return configureIfMatch(ANYHOST_VALUE, url);

        }

    }

    return url;

}
</code></pre>
<p>configureIfMatch() 方法会排除匹配 URL 中不可动态修改的参数，并调用 Configurator 子类的 doConfigurator() 方法重写原始 URL，具体实现如下：</p>
<pre><code>private URL configureIfMatch(String host, URL url) {

    if (ANYHOST_VALUE.equals(configuratorUrl.getHost()) || host.equals(configuratorUrl.getHost())) { // 匹配host

        String providers = configuratorUrl.getParameter(OVERRIDE_PROVIDERS_KEY);

        if (StringUtils.isEmpty(providers) || providers.contains(url.getAddress()) || providers.contains(ANYHOST_VALUE)) { 

            String configApplication = configuratorUrl.getParameter(APPLICATION_KEY,

                    configuratorUrl.getUsername());

            String currentApplication = url.getParameter(APPLICATION_KEY, url.getUsername());

            if (configApplication == null || ANY_VALUE.equals(configApplication)

                    || configApplication.equals(currentApplication)) { // 匹配application

                // 排除不能动态修改的属性，其中包括category、check、dynamic、enabled还有以~开头的属性

                Set&lt;String&gt; conditionKeys = new HashSet&lt;String&gt;(); 

                conditionKeys.add(CATEGORY_KEY);

                conditionKeys.add(Constants.CHECK_KEY);

                conditionKeys.add(DYNAMIC_KEY);

                conditionKeys.add(ENABLED_KEY);

                conditionKeys.add(GROUP_KEY);

                conditionKeys.add(VERSION_KEY);

                conditionKeys.add(APPLICATION_KEY);

                conditionKeys.add(SIDE_KEY);

                conditionKeys.add(CONFIG_VERSION_KEY);

                conditionKeys.add(COMPATIBLE_CONFIG_KEY);

                conditionKeys.add(INTERFACES);

                for (Map.Entry&lt;String, String&gt; entry : configuratorUrl.getParameters().entrySet()) {

                    String key = entry.getKey();

                    String value = entry.getValue();

                    if (key.startsWith(&quot;~&quot;) || APPLICATION_KEY.equals(key) || SIDE_KEY.equals(key)) {

                        conditionKeys.add(key);

                        // 如果配置URL与原URL中以~开头的参数值不相同，则不使用该配置URL重写原URL

                        if (value != null &amp;&amp; !ANY_VALUE.equals(value)

                                &amp;&amp; !value.equals(url.getParameter(key.startsWith(&quot;~&quot;) ? key.substring(1) : key))) {

                            return url;

                        }

                    }

                }

                // 移除配置URL不支持动态配置的参数之后，调用Configurator子类的doConfigure方法重新生成URL

                return doConfigure(url, configuratorUrl.removeParameters(conditionKeys));

            }

        }

    }

    return url;

}
</code></pre>
<p>我们再反过来仔细审视一下 AbstractConfigurator.configure() 方法中针对 2.7.0 版本之后动态配置的处理，其中会根据 side 参数明确判断配置 URL 和原始 URL 属于 Consumer 端还是 Provider 端，判断逻辑也更加清晰。匹配之后的具体替换过程同样是调用 configureIfMatch() 方法实现的，这里不再重复。</p>
<p>Configurator 的两个子类实现非常简单。在 OverrideConfigurator 的 doConfigure() 方法中，会直接用配置 URL 中剩余的全部参数，覆盖原始 URL 中的相应参数，具体实现如下：</p>
<pre><code>public URL doConfigure(URL currentUrl, URL configUrl) {

    // 直接调用addParameters()方法，进行覆盖

    return currentUrl.addParameters(configUrl.getParameters());

}
</code></pre>
<p>在 AbsentConfigurator 的 doConfigure() 方法中，会尝试用配置 URL 中的参数添加到原始 URL 中，如果原始 URL 中已经有了该参数是不会被覆盖的，具体实现如下：</p>
<pre><code>public URL doConfigure(URL currentUrl, URL configUrl) {

    // 直接调用addParametersIfAbsent()方法尝试添加参数

    return currentUrl.addParametersIfAbsent(configUrl.getParameters());

}
</code></pre>
<p>到这里，Dubbo 2.7.0 版本之前的<strong>动态配置核心实现</strong>就介绍完了，其中我们也简单涉及了 Dubbo 2.7.0 版本之后一些逻辑，只不过没有全面介绍 Dubbo 2.7.0 之后的配置格式以及核心处理逻辑，不用担心，这些内容我们将会在后面的“配置中心”章节继续深入分析。</p>
<h3>总结</h3>
<p>本课时我们主要介绍了 Dubbo 中配置相关的实现。我们首先通过示例分析了 configurators 目录中涉及的 override 协议 URL、absent 协议 URL 的格式以及各个参数的含义，然后还详细讲解了 Dubbo 解析 configurator URL 得到的 Configurator 对象，以及 Configurator 覆盖 Provider URL 各个参数的具体实现。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="33&#32;&#32;路由机制：请求到底怎么走，它说了算（下）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="35&#32;&#32;负载均衡：公平公正物尽其用的负载均衡策略，这里都有（上）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433facaf6d70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
