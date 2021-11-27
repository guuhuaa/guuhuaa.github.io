<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>27  加餐：直击 Dubbo “心脏”，带你一起探秘 Invoker（下）.md</title>
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

                    <a class="current-tab" href="27&#32;&#32;加餐：直击&#32;Dubbo&#32;“心脏”，带你一起探秘&#32;Invoker（下）.md">27  加餐：直击 Dubbo “心脏”，带你一起探秘 Invoker（下）.md</a>
                    

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
                        <div><h1>27  加餐：直击 Dubbo “心脏”，带你一起探秘 Invoker（下）</h1>
<p>关于 DubboInvoker，在发送完<strong>oneway 请求</strong>之后，会立即创建一个已完成状态的 AsyncRpcResult 对象（主要是其中的 responseFuture 是已完成状态）。这在上一课时我们已经讲解过了。</p>
<p>本课时我们将继续介绍 DubboInvoker 处理 twoway 请求和响应的相关实现，其中会涉及响应解码、同步/异步响应等相关内容；完成对 DubboInvoker 的分析之后，我们还会介绍 Dubbo 中与 Listener、Filter 相关的 Invoker 装饰器。</p>
<h3>再探 DubboInvoker</h3>
<p>那 DubboInvoker 对<strong>twoway 请求</strong>的处理又是怎样的呢？接下来我们就来重点介绍下。首先，DubboInvoker 会调用 getCallbackExecutor() 方法，根据不同的 InvokeMode 返回不同的线程池实现，代码如下：</p>
<pre><code>protected ExecutorService getCallbackExecutor(URL url, Invocation inv) {

    ExecutorService sharedExecutor = ExtensionLoader.getExtensionLoader(ExecutorRepository.class).getDefaultExtension().getExecutor(url);

    if (InvokeMode.SYNC == RpcUtils.getInvokeMode(getUrl(), inv)) {

        return new ThreadlessExecutor(sharedExecutor);

    } else {

        return sharedExecutor;

    }

}
</code></pre>
<p>InvokeMode 有三个可选值，分别是 SYNC、ASYNC 和 FUTURE。这里对于 SYNC 模式返回的线程池是 ThreadlessExecutor，至于其他两种异步模式，会根据 URL 选择对应的共享线程池。</p>
<p><strong>SYNC 表示同步模式</strong>，是 Dubbo 的默认调用模式，具体含义如下图所示，客户端发送请求之后，客户端线程会阻塞等待服务端返回响应。</p>
<p><img src="assets/CgqCHl-X8UOAOTRbAACy-uBf52M689.png" alt="Lark20201027-180625.png" /></p>
<p>SYNC 调用模式图</p>
<p>在拿到线程池之后，DubboInvoker 就会调用 ExchangeClient.request() 方法，将 Invocation 包装成 Request 请求发送出去，同时会创建相应的 DefaultFuture 返回。注意，这里还加了一个回调，取出其中的 AppResponse 对象。AppResponse 表示的是服务端返回的具体响应，其中有三个字段。</p>
<ul>
<li>result（Object 类型）：响应结果，也就是服务端返回的结果值，注意，这是一个业务上的结果值。例如，在我们前面第 01 课时的 Demo 示例（即 dubbo-demo 模块中的 Demo）中，Provider 端 DemoServiceImpl 返回的 “Hello Dubbo xxx” 这一串字符串。</li>
<li>exception（Throwable 类型）：服务端返回的异常信息。</li>
<li>attachments（Map&lt;String, Object&gt; 类型）：服务端返回的附加信息。</li>
</ul>
<p>这里请求返回的 AppResponse 你可能不太熟悉，但是其子类 DecodeableRpcResult 你可能就有点眼熟了，DecodeableRpcResult 表示的是一个响应，与其对应的是 DecodeableRpcInvocation（它表示的是请求）。在第 24 课时介绍 DubboCodec 对 Dubbo 请求体的编码流程中，我们已经详细介绍过 DecodeableRpcInvocation 了，你可以回顾一下 DubboCodec 的 decodeBody() 方法，就会发现 DecodeableRpcResult 的“身影”。</p>
<h4>1. DecodeableRpcResult</h4>
<p>DecodeableRpcResult 解码核心流程大致如下：</p>
<ul>
<li>首先，确定当前使用的序列化方式，并对字节流进行解码。</li>
<li>然后，读取一个 byte 的标志位，其可选值有六种枚举，下面我们就以其中的 RESPONSE_VALUE_WITH_ATTACHMENTS 为例进行分析。</li>
<li>标志位为 RESPONSE_VALUE_WITH_ATTACHMENTS 时，会先通过 handleValue() 方法处理返回值，其中会根据 RpcInvocation 中记录的返回值类型读取返回值，并设置到 result 字段。</li>
<li>最后，再通过 handleAttachment() 方法读取返回的附加信息，并设置到 DecodeableRpcResult 的 attachments 字段中。</li>
</ul>
<pre><code>public Object decode(Channel channel, InputStream input) throws IOException {

    // 反序列化

    ObjectInput in = CodecSupport.getSerialization(channel.getUrl(), serializationType)

            .deserialize(channel.getUrl(), input);

    byte flag = in.readByte(); // 读取一个byte的标志位

    // 根据标志位判断当前结果中包含的信息，并调用不同的方法进行处理

    switch (flag) { 

        case DubboCodec.RESPONSE_NULL_VALUE:

            break;

        case DubboCodec.RESPONSE_VALUE:

            handleValue(in);

            break;

        case DubboCodec.RESPONSE_WITH_EXCEPTION:

            handleException(in);

            break;

        case DubboCodec.RESPONSE_NULL_VALUE_WITH_ATTACHMENTS:

            handleAttachment(in);

            break;

        case DubboCodec.RESPONSE_VALUE_WITH_ATTACHMENTS:

            handleValue(in);

            handleAttachment(in);

            break;

        case DubboCodec.RESPONSE_WITH_EXCEPTION_WITH_ATTACHMENTS:

        default:

            throw new IOException(&quot;...&quot; );

    }

    if (in instanceof Cleanable) {

        ((Cleanable) in).cleanup();

    }

    return this;

}
</code></pre>
<p>decode() 方法中其他分支的代码这里就不再展示了，你若感兴趣的话可以参考 DecodeableRpcResult 源码进行分析。</p>
<h4>2. AsyncRpcResult</h4>
<p>在 DubboInvoker 中还有一个 <strong>AsyncRpcResult 类，它表示的是一个异步的、未完成的 RPC 调用，其中会记录对应 RPC 调用的信息</strong>（例如，关联的 RpcContext 和 Invocation 对象），包括以下几个核心字段。</p>
<ul>
<li>responseFuture（CompletableFuture<code>&lt;AppResponse&gt;</code> 类型）：这个 responseFuture 字段与前文提到的 DefaultFuture 有紧密的联系，是 DefaultFuture 回调链上的一个 Future。后面 AsyncRpcResult 之上添加的回调，实际上都是添加到这个 Future 之上。</li>
<li>storedContext、storedServerContext（RpcContext 类型）：用于存储相关的 RpcContext 对象。我们知道 RpcContext 是与线程绑定的，而真正执行 AsyncRpcResult 上添加的回调方法的线程可能先后处理过多个不同的 AsyncRpcResult，所以我们需要传递并保存当前的 RpcContext。</li>
<li>executor（Executor 类型）：此次 RPC 调用关联的线程池。</li>
<li>invocation（Invocation 类型）：此次 RPC 调用关联的 Invocation 对象。</li>
</ul>
<p>在 AsyncRpcResult 构造方法中，除了接收发送请求返回的 CompletableFuture<code>&lt;AppResponse&gt;</code> 对象，还会将当前的 RpcContext 保存到 storedContext 和 storedServerContext 中，具体实现如下：</p>
<pre><code>public AsyncRpcResult(CompletableFuture&lt;AppResponse&gt; future, Invocation invocation) {

    this.responseFuture = future;

    this.invocation = invocation;

    this.storedContext = RpcContext.getContext();

    this.storedServerContext = RpcContext.getServerContext();

}
</code></pre>
<p>通过 whenCompleteWithContext() 方法，我们可以为 AsyncRpcResult 添加回调方法，而这个回调方法会被包装一层并注册到 responseFuture 上，具体实现如下：</p>
<pre><code>public Result whenCompleteWithContext(BiConsumer&lt;Result, Throwable&gt; fn) {

    // 在responseFuture之上注册回调

    this.responseFuture = this.responseFuture.whenComplete((v, t) -&gt; {

        beforeContext.accept(v, t);

        fn.accept(v, t);

        afterContext.accept(v, t);

    });

    return this;

}
</code></pre>
<p>这里的 beforeContext 首先会将当前线程的 RpcContext 记录到 tmpContext 中，然后将构造函数中存储的 RpcContext 设置到当前线程中，为后面的回调执行做准备；而 afterContext 则会恢复线程原有的 RpcContext。具体实现如下：</p>
<pre><code>private RpcContext tmpContext;

private RpcContext tmpServerContext;

private BiConsumer&lt;Result, Throwable&gt; beforeContext = (appResponse, t) -&gt; {

    // 将当前线程的 RpcContext 记录到 tmpContext 中

    tmpContext = RpcContext.getContext();

    tmpServerContext = RpcContext.getServerContext();

    // 将构造函数中存储的 RpcContext 设置到当前线程中

    RpcContext.restoreContext(storedContext);

    RpcContext.restoreServerContext(storedServerContext);

};

private BiConsumer&lt;Result, Throwable&gt; afterContext = (appResponse, t) -&gt; {

    // 将tmpContext中存储的RpcContext恢复到当前线程绑定的RpcContext

    RpcContext.restoreContext(tmpContext);

    RpcContext.restoreServerContext(tmpServerContext);

};
</code></pre>
<p>这样，AsyncRpcResult 就可以处于不断地添加回调而不丢失 RpcContext 的状态。总之，AsyncRpcResult 整个就是为异步请求设计的。</p>
<p>在前面的分析中我们看到，RpcInvocation.InvokeMode 字段中可以指定调用为 SYNC 模式，也就是同步调用模式，那 AsyncRpcResult 这种异步设计是如何支持同步调用的呢？ 在 AbstractProtocol.refer() 方法中，Dubbo 会将 DubboProtocol.protocolBindingRefer() 方法返回的 Invoker 对象（即 DubboInvoker 对象）用 AsyncToSyncInvoker 封装一层。</p>
<p><strong>AsyncToSyncInvoker 是 Invoker 的装饰器，负责将异步调用转换成同步调用</strong>，其 invoke() 方法的核心实现如下：</p>
<pre><code>public Result invoke(Invocation invocation) throws RpcException {

    Result asyncResult = invoker.invoke(invocation);

    if (InvokeMode.SYNC == ((RpcInvocation) invocation).getInvokeMode()) {

        // 调用get()方法，阻塞等待响应返回

        asyncResult.get(Integer.MAX_VALUE, TimeUnit.MILLISECONDS);

    }

    return asyncResult;

}
</code></pre>
<p>其实 AsyncRpcResult.get() 方法底层调用的就是 responseFuture 字段的 get() 方法，对于同步请求来说，会先调用 ThreadlessExecutor.waitAndDrain() 方法阻塞等待响应返回，具体实现如下所示：</p>
<pre><code>public Result get() throws InterruptedException, ExecutionException {

    if (executor != null &amp;&amp; executor instanceof ThreadlessExecutor) {

        // 针对ThreadlessExecutor的特殊处理，这里调用waitAndDrain()等待响应

        ThreadlessExecutor threadlessExecutor = (ThreadlessExecutor) executor;

        threadlessExecutor.waitAndDrain();

    }

    // 非ThreadlessExecutor线程池的场景中，则直接调用Future(最底层是DefaultFuture)的get()方法阻塞

    return responseFuture.get();

}
</code></pre>
<p>ThreadlessExecutor 针对同步请求的优化，我们在前面的第 20 课时已经详细介绍过了，这里不再重复。</p>
<p>最后要说明的是，<strong>AsyncRpcResult 实现了 Result 接口</strong>，如下图所示：</p>
<p><img src="assets/Ciqc1F-WqdmAbppOAABOGWzVljY775.png" alt="Drawing 1.png" /></p>
<p>AsyncRpcResult 继承关系图</p>
<p>AsyncRpcResult 对 Result 接口的实现，例如，getValue() 方法、recreate() 方法、getAttachments() 方法等，都会先调用 getAppResponse() 方法从 responseFuture 中拿到 AppResponse 对象，然后再调用其对应的方法。这里我们以 recreate() 方法为例，简单分析一下：</p>
<pre><code>public Result getAppResponse() { // 省略异常处理的逻辑

    if (responseFuture.isDone()) { // 检测responseFuture是否已完成

        return responseFuture.get(); // 获取AppResponse

    }

    // 根据调用方法的返回值，生成默认值

    return createDefaultValue(invocation); 

}

public Object recreate() throws Throwable {

    RpcInvocation rpcInvocation = (RpcInvocation) invocation;

    if (InvokeMode.FUTURE == rpcInvocation.getInvokeMode()) {

        return RpcContext.getContext().getFuture();

    }

    // 调用AppResponse.recreate()方法

    return getAppResponse().recreate(); 

}
</code></pre>
<p>AppResponse.recreate() 方法实现比较简单，如下所示：</p>
<pre><code>public Object recreate() throws Throwable {

    if (exception != null) { // 存在异常则直接抛出异常

        // 省略处理堆栈信息的逻辑

        throw exception; 

    }

    return result; // 正常返回无异常时，直接返回result

}
</code></pre>
<p>这里我们注意到，在 recreate() 方法中，AsyncRpcResult 会对 FUTURE 特殊处理。如果服务接口定义的返回参数是 CompletableFuture，则属于 FUTURE 模式，<strong>FUTURE 模式也属于 Dubbo 提供的一种异步调用方式，只不过是服务端异步</strong>。FUTURE 模式下拿到的 CompletableFuture 对象其实是在 AbstractInvoker 中塞到 RpcContext 中的，在 AbstractInvoker.invoke() 方法中有这么一段代码：</p>
<pre><code>RpcContext.getContext().setFuture(

    new FutureAdapter(asyncResult.getResponseFuture()));
</code></pre>
<p>这里拿到的其实就是 AsyncRpcResult 中 responseFuture，即前面介绍的 DefaultFuture。可见，<strong>无论是 SYNC 模式、ASYNC 模式还是 FUTURE 模式，都是围绕 DefaultFuture 展开的。</strong></p>
<p>其实，在 Dubbo 2.6.x 及之前的版本提供了一定的异步编程能力，但其异步方式存在如下一些问题：</p>
<ul>
<li>Future 获取方式不够直接，业务需要从 RpcContext 中手动获取。</li>
<li>Future 接口无法实现自动回调，而自定义 ResponseFuture（这是 Dubbo 2.6.x 中类）虽支持回调，但支持的异步场景有限，并且还不支持 Future 间的相互协调或组合等。</li>
<li>不支持 Provider 端异步。</li>
</ul>
<p>Dubbo 2.6.x 及之前版本中使用的 Future 是在 Java 5 中引入的，所以存在以上一些功能设计上的问题；而在 Java 8 中引入的 CompletableFuture 进一步丰富了 Future 接口，很好地解决了这些问题。<strong>Dubbo 在 2.7.0 版本已经升级了对 Java 8 的支持，同时基于 CompletableFuture 对当前的异步功能进行了增强，弥补了上述不足。</strong></p>
<p>因为 CompletableFuture 实现了 CompletionStage 和 Future 接口，所以它还是可以像以前一样通过 get() 阻塞或者 isDone() 方法轮询的方式获得结果，这就保证了同步调用依旧可用。当然，在实际工作中，不是很建议用 get() 这样阻塞的方式来获取结果，因为这样就丢失了异步操作带来的性能提升。</p>
<p>另外，CompletableFuture 提供了良好的回调方法，例如，whenComplete()、whenCompleteAsync() 等方法都可以在逻辑完成后，执行该方法中添加的 action 逻辑，实现回调的逻辑。同时，CompletableFuture 很好地支持了 Future 间的相互协调或组合，例如，thenApply()、thenApplyAsync() 等方法。</p>
<p>正是由于 CompletableFuture 的增强，我们可以更加流畅地使用回调，不必因为等待一个响应而阻塞着调用线程，而是通过前面介绍的方法告诉 CompletableFuture 完成当前逻辑之后，就去执行某个特定的函数。在 Demo 示例（即 dubbo-demo 模块中的 Demo ）中，返回 CompletableFuture 的 sayHelloAsync() 方法就是使用的 FUTURE 模式。</p>
<p>好了，DubboInvoker 涉及的同步调用、异步调用的原理和底层实现就介绍到这里了，我们可以通过一张流程图进行简单总结，如下所示：</p>
<p><img src="assets/Ciqc1F-X8WuACaAKAAEb-X6qf4Y710.png" alt="Lark20201027-180621.png" /></p>
<p>DubboInvoker 核心流程图</p>
<p>在 Client 端发送请求时，首先会创建对应的 DefaultFuture（其中记录了请求 ID 等信息），然后依赖 Netty 的异步发送特性将请求发送到 Server 端。需要说明的是，这整个发送过程是不会阻塞任何线程的。之后，将 DefaultFuture 返回给上层，在这个返回过程中，DefaultFuture 会被封装成 AsyncRpcResult，同时也可以添加回调函数。</p>
<p>当 Client 端接收到响应结果的时候，会交给关联的线程池（ExecutorService）或是业务线程（使用 ThreadlessExecutor 场景）进行处理，得到 Server 返回的真正结果。拿到真正的返回结果后，会将其设置到 DefaultFuture 中，并调用 complete() 方法将其设置为完成状态。此时，就会触发前面注册在 DefaulFuture 上的回调函数，执行回调逻辑。</p>
<h3>Invoker 装饰器</h3>
<p>除了上面介绍的 DubboInvoker 实现之外，Invoker 接口还有很多装饰器实现，这里重点介绍 Listener、Filter 相关的 Invoker 实现。</p>
<h4>1. ListenerInvokerWrapper</h4>
<p>在前面的第 23 课时中简单提到过 InvokerListener 接口，我们可以提供其实现来监听 refer 事件以及 destroy 事件，相应地要实现 referred() 方法以及 destroyed() 方法。</p>
<p>ProtocolListenerWrapper 是 Protocol 接口的实现之一，如下图所示：</p>
<p><img src="assets/CgqCHl-WqfyAZ0TzAAAbeTUMLT0465.png" alt="Drawing 3.png" /></p>
<p>ProtocolListenerWrapper 继承关系图</p>
<p>ProtocolListenerWrapper 本身是 Protocol 接口的装饰器，在其 export() 方法和 refer() 方法中，会分别在原有 Invoker 基础上封装一层 ListenerExporterWrapper 和 ListenerInvokerWrapper。</p>
<p><strong>ListenerInvokerWrapper 是 Invoker 的装饰器</strong>，其构造方法参数列表中除了被修饰的 Invoker 外，还有 InvokerListener 列表，在构造方法内部会遍历整个 InvokerListener 列表，并调用每个 InvokerListener 的 referred() 方法，通知它们 Invoker 被引用的事件。核心逻辑如下：</p>
<pre><code>public ListenerInvokerWrapper(Invoker&lt;T&gt; invoker, List&lt;InvokerListener&gt; listeners) {

    this.invoker = invoker; // 底层被修饰的Invoker对象

    this.listeners = listeners; // 监听器集合

    if (CollectionUtils.isNotEmpty(listeners)) {

        for (InvokerListener listener : listeners) {

            if (listener != null) {// 在服务引用过程中触发全部InvokerListener监听器

                listener.referred(invoker); 

            }

        }

    }

}
</code></pre>
<p>在 ListenerInvokerWrapper.destroy() 方法中，首先会调用被修饰 Invoker 对象的 destroy() 方法，之后循环调用全部 InvokerListener 的 destroyed() 方法，通知它们该 Invoker 被销毁的事件，具体实现比较简单，这里就不再展示，你若感兴趣的话可以<a href="https://github.com/apache/dubbo/tree/dubbo-2.7.7">参考源码</a>进行学习。</p>
<p>与 InvokerListener 对应的是 ExporterListener 监听器，其实现类可以通过实现 exported() 方法和 unexported() 方法监听服务暴露事件以及取消暴露事件。</p>
<p>相应地，在 ProtocolListenerWrapper 的 export() 方法中也会在原有 Invoker 之上用 ListenerExporterWrapper 进行一层封装，ListenerExporterWrapper 的构造方法中会循环调用全部 ExporterListener 的 exported() 方法，通知其服务暴露的事件，核心逻辑如下所示：</p>
<pre><code>public ListenerExporterWrapper(Exporter&lt;T&gt; exporter, List&lt;ExporterListener&gt; listeners) {

    this.exporter = exporter;

    this.listeners = listeners;

    if (CollectionUtils.isNotEmpty(listeners)) {

        RuntimeException exception = null;

        for (ExporterListener listener : listeners) {

            if (listener != null) {

                listener.exported(this);

            }

        }

    }

}
</code></pre>
<p>ListenerExporterWrapper.unexported() 方法的逻辑与上述 exported() 方法的实现基本类似，这里不再赘述。</p>
<p>这里介绍的 ListenerInvokerWrapper 和 ListenerExporterWrapper 都是被 @SPI 注解修饰的，我们可以提供相应的扩展实现，然后配置 SPI 文件监听这些事件。</p>
<h4>2. Filter 相关的 Invoker 装饰器</h4>
<p>Filter 接口是 Dubbo 为用户提供的一个非常重要的扩展接口，将各个 Filter 串联成 Filter 链并与 Invoker 实例相关。构造 Filter 链的核心逻辑位于 ProtocolFilterWrapper.buildInvokerChain() 方法中，ProtocolFilterWrapper 的 refer() 方法和 export() 方法都会调用该方法。</p>
<p>buildInvokerChain() 方法的核心逻辑如下：</p>
<ul>
<li>首先会根据 URL 中携带的配置信息，确定当前激活的 Filter 扩展实现有哪些，形成 Filter 集合。</li>
<li>遍历 Filter 集合，将每个 Filter 实现封装成一个匿名 Invoker，在这个匿名 Invoker 中，会调用 Filter 的 invoke() 方法执行 Filter 的逻辑，然后由 Filter 内部的逻辑决定是否将调用传递到下一个 Filter 执行。</li>
</ul>
<p>buildInvokerChain() 方法的具体实现如下：</p>
<pre><code>private static &lt;T&gt; Invoker&lt;T&gt; buildInvokerChain(final Invoker&lt;T&gt; invoker, String key, String group) {

    Invoker&lt;T&gt; last = invoker;

    // 根据 URL 中携带的配置信息，确定当前激活的 Filter 扩展实现有哪些，形成 Filter 集合

    List&lt;Filter&gt; filters = ExtensionLoader.getExtensionLoader(Filter.class).getActivateExtension(invoker.getUrl(), key, group);

    if (!filters.isEmpty()) {

        for (int i = filters.size() - 1; i &gt;= 0; i--) {

            final Filter filter = filters.get(i);

            final Invoker&lt;T&gt; next = last;

            // 遍历 Filter 集合，将每个 Filter 实现封装成一个匿名 Invoker

            last = new Invoker&lt;T&gt;() {

                @Override

                public Result invoke(Invocation invocation) throws RpcException {

                    Result asyncResult;

                    try {

                        // 调用 Filter 的 invoke() 方法执行 Filter 的逻辑，然后由 Filter 内部的逻辑决定是否将调用传递到下一个 Filter 执行

                        asyncResult = filter.invoke(next, invocation);

                    } catch (Exception e) {

                        ... // 省略异常时监听器的逻辑

                    } finally {

                    }

                    return asyncResult.whenCompleteWithContext((r, t) -&gt; {

                        ... // 省略监听器的处理逻辑

                    });

                }

            };

        }

    }

    return last;

}
</code></pre>
<p>在 Filter 接口内部还定义了一个 Listener 接口，有一些 Filter 实现会同时实现这个内部 Listener 接口，当 invoke() 方法执行正常结束时，会调用该 Listener 的 onResponse() 方法进行通知；当 invoke() 方法执行出现异常时，会调用该 Listener 的 onError() 方法进行通知。</p>
<p>另外，还有一个 ListenableFilter 抽象类，它继承了 Filter 接口，在原有 Filter 的基础上添加了一个 listeners 集合（ConcurrentMap&lt;Invocation, Filter.Listener&gt; 集合）用来记录一次请求需要触发的监听器。需要注意的是，在执行 invoke() 调用之前，我们可以调用 addListener() 方法添加 Filter.Listener 实例进行监听，完成一次 invoke() 方法之后，这些添加的 Filter.Listener 实例就会立即从 listeners 集合中删除，也就是说，这些 Filter.Listener 实例不会在调用之间共享。</p>
<h3>总结</h3>
<p>本课时主要介绍的是 Dubbo 中 Invoker 接口的核心实现，这也是 Dubbo 最核心的实现之一。</p>
<p>紧接上一课时，我们分析了 DubboInvoker 对 twoway 请求的处理逻辑，其中展开介绍了涉及的 DecodeableRpcResult 以及 AsyncRpcResult 等核心类，深入讲解了 Dubbo 的同步、异步调用实现原理，说明了 Dubbo 在 2.7.x 版本之后的相关改进。最后，我们还介绍了 Invoker 接口的几个装饰器，其中涉及用于注册监听器的 ListenerInvokerWrapper 以及 Filter 相关的 Invoker 装饰器。</p>
<p>下一课时，我们将深入介绍 Dubbo RPC 层中代理的相关实现。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="26&#32;&#32;加餐：直击&#32;Dubbo&#32;“心脏”，带你一起探秘&#32;Invoker（上）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="28&#32;&#32;复杂问题简单化，代理帮你隐藏了多少底层细节？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433f7d8fe070ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
