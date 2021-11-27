<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>23  核心接口介绍，RPC 层骨架梳理.md</title>
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

                    <a class="current-tab" href="23&#32;&#32;核心接口介绍，RPC&#32;层骨架梳理.md">23  核心接口介绍，RPC 层骨架梳理.md</a>
                    

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
                        <div><h1>23  核心接口介绍，RPC 层骨架梳理</h1>
<p>在前面的课程中，我们深入介绍了 Dubbo 架构中的 Dubbo Remoting 层的相关内容，了解了 Dubbo 底层的网络模型以及线程模型。从本课时开始，我们就开始介绍 Dubbo Remoting 上面的一层—— Protocol 层（如下图所示），<strong>Protocol 层是 Remoting 层的使用者</strong>，会通过 Exchangers 门面类创建 ExchangeClient 以及 ExchangeServer，还会创建相应的 ChannelHandler 实现以及 Codec2 实现并交给 Exchange 层进行装饰。</p>
<p><img src="assets/Ciqc1F-FS2eAdVorABDINpNLpXY061.png" alt="Drawing 0.png" /></p>
<p>Dubbo 架构中 Protocol 层的位置图</p>
<p><strong>Protocol 层在 Dubbo 源码中对应的是 dubbo-rpc 模块</strong>，该模块的结构如下图所示：</p>
<p><img src="assets/Ciqc1F-FS4aAMyvkAABpKhWTC9Q132.png" alt="Drawing 1.png" /></p>
<p>dubbo-rpc 模块结构图</p>
<p>我们可以看到有很多模块，和 dubbo-remoting 模块类似，其中 <strong>dubbo-rpc-api 是对具体协议、服务暴露、服务引用、代理等的抽象，是整个 Protocol 层的核心</strong>。剩余的模块，例如，dubbo-rpc-dubbo、dubbo-rpc-grpc、dubbo-rpc-http 等，都是 Dubbo 支持的具体协议，可以看作dubbo-rpc-api 模块的具体实现。</p>
<h3>dubbo-rpc-api</h3>
<p>这里我们首先来看 dubbo-rpc-api 模块的包结构，如下图所示：</p>
<p><img src="assets/CgqCHl-FS5CAP7kCAADYKrhf28A273.png" alt="Drawing 2.png" /></p>
<p>dubbo-rpc-api 模块的包结构图</p>
<p>根据上图展示的 dubbo-rpc-api 模块的结构，我们可以看到 dubbo-rpc-api 模块包括了以下几个核心包。</p>
<ul>
<li>filter 包：在进行服务引用时会进行一系列的过滤，其中包括了很多过滤器。</li>
<li>listener 包：在服务发布和服务引用的过程中，我们可以添加一些 Listener 来监听相应的事件，与 Listener 相关的接口 Adapter、Wrapper 实现就在这个包内。</li>
<li>protocol 包：一些实现了 Protocol 接口以及 Invoker 接口的抽象类位于该包之中，它们主要是为 Protocol 接口的具体实现以及 Invoker 接口的具体实现提供一些公共逻辑。</li>
<li>proxy 包：提供了创建代理的能力，在这个包中支持 JDK 动态代理以及 Javassist 字节码两种方式生成本地代理类。</li>
<li>support 包：包括了 RpcUtils 工具类、Mock 相关的 Protocol 实现以及 Invoker 实现。</li>
</ul>
<p>没有在上述 package 中的接口和类，是更为核心的抽象接口，上述 package 内的类更多的是这些接口的实现类。下面我们就来介绍这些在 org.apache.dubbo.rpc 包下的核心接口。</p>
<h3>核心接口</h3>
<p>在 Dubbo RPC 层中涉及的核心接口有 Invoker、Invocation、Protocol、Result、Exporter、ProtocolServer、Filter 等，这些接口分别抽象了 Dubbo RPC 层的不同概念，看似相互独立，但又相互协同，一起构建出了 DubboRPC 层的骨架。下面我们将逐一介绍这些核心接口的含义。</p>
<p>首先要介绍的是 Dubbo 中非常重要的一个接口——<strong>Invoker 接口</strong>。可以说，Invoker 渗透在整个 Dubbo 代码实现里，Dubbo 中的很多设计思路都会向 Invoker 这个概念靠拢，但这对于刚接触这部分代码的同学们来说，可能不是很友好。</p>
<p>这里我们借助如下这样一个精简的示意图来对比说明两种最关键的 Invoker：服务提供 Invoker 和服务消费 Invoker。</p>
<p><img src="assets/Ciqc1F-FWQuAb1ypAAC0qPg0sWQ701.png" alt="Lark20201013-153553.png" /></p>
<p>Invoker 核心示意图</p>
<p>以 dubbo-demo-annotation-consumer 这个示例项目中的 Consumer 为例，它会拿到一个 DemoService 对象，如下所示，这其实是一个代理（即上图中的 Proxy），这个 Proxy 底层就会通过 Invoker 完成网络调用：</p>
<pre><code>@Component(&quot;demoServiceComponent&quot;)

public class DemoServiceComponent implements DemoService {

    @Reference

    private DemoService demoService;

    @Override

    public String sayHello(String name) {

        return demoService.sayHello(name);

    }

}
</code></pre>
<p>紧接着我们再来看一个 dubbo-demo-annotation-provider 示例中的 Provider 实现：</p>
<pre><code>@Service

public class DemoServiceImpl implements DemoService {

    @Override

    public String sayHello(String name) {

        return &quot;Hello &quot; + name + &quot;, response from provider: &quot; + RpcContext.getContext().getLocalAddress();

    }

}
</code></pre>
<p>这里的 DemoServiceImpl 类会被封装成为一个 AbstractProxyInvoker 实例，并新生成对应的 Exporter 实例。当 Dubbo Protocol 层收到一个请求之后，会找到这个 Exporter 实例，并调用其对应的 AbstractProxyInvoker 实例，从而完成 Provider 逻辑的调用。这里我先帮你找出了最重要的两类 Invoker ，简单介绍了它们工作场景，当然 Dubbo 中还有其他类型的 Invoker，后面我们再一一介绍。</p>
<p>下面来看 Invoker 这个接口的具体定义，如下所示：</p>
<pre><code>public interface Invoker&lt;T&gt; extends Node {

    // 服务接口

    Class&lt;T&gt; getInterface();

    // 进行一次调用，也有人称之为一次&quot;会话&quot;，你可以理解为一次调用

    Result invoke(Invocation invocation) throws RpcException;

}
</code></pre>
<p><strong>Invocation 接口</strong>是 Invoker.invoke() 方法的参数，抽象了一次 RPC 调用的目标服务和方法信息、相关参数信息、具体的参数值以及一些附加信息，具体定义如下：</p>
<pre><code>public interface Invocation {

    // 调用Service的唯一标识

    String getTargetServiceUniqueName();

    // 调用的方法名称

    String getMethodName();

    // 调用的服务名称

    String getServiceName();

    // 参数类型集合

    Class&lt;?&gt;[] getParameterTypes();

    // 参数签名集合

    default String[] getCompatibleParamSignatures() {

        return Stream.of(getParameterTypes())

                .map(Class::getName)

                .toArray(String[]::new);

    }

    // 此次调用具体的参数值

    Object[] getArguments();

    // 此次调用关联的Invoker对象

    Invoker&lt;?&gt; getInvoker();

    // Invoker对象可以设置一些KV属性，这些属性并不会传递给Provider

    Object put(Object key, Object value);

    Object get(Object key);

    Map&lt;Object, Object&gt; getAttributes();

    // Invocation可以携带一个KV信息作为附加信息，一并传递给Provider，

    // 注意与 attribute 的区分

    Map&lt;String, String&gt; getAttachments();

    Map&lt;String, Object&gt; getObjectAttachments();

    void setAttachment(String key, String value);

    void setAttachment(String key, Object value);

    void setObjectAttachment(String key, Object value);

    void setAttachmentIfAbsent(String key, String value);

    void setAttachmentIfAbsent(String key, Object value);

    void setObjectAttachmentIfAbsent(String key, Object value);

    String getAttachment(String key);

    Object getObjectAttachment(String key);

    String getAttachment(String key, String defaultValue);

    Object getObjectAttachment(String key, Object defaultValue);

}
</code></pre>
<p><strong>Result 接口</strong>是 Invoker.invoke() 方法的返回值，抽象了一次调用的返回值，其中包含了被调用方返回值（或是异常）以及附加信息，我们也可以添加回调方法，在 RPC 调用方法结束时会触发这些回调。Result 接口的具体定义如下：</p>
<pre><code>public interface Result extends Serializable {

    // 获取/设置此次调用的返回值

    Object getValue();

    void setValue(Object value);

    // 如果此次调用发生异常，则可以通过下面三个方法获取

    Throwable getException();

    void setException(Throwable t);

    boolean hasException();

    // recreate()方法是一个复合操作，如果此次调用发生异常，则直接抛出异常，

    // 如果没有异常，则返回结果

    Object recreate() throws Throwable;

    // 添加一个回调，当RPC调用完成时，会触发这里添加的回调

    Result whenCompleteWithContext(BiConsumer&lt;Result, Throwable&gt; fn);

    &lt;U&gt; CompletableFuture&lt;U&gt; thenApply(Function&lt;Result, ? extends U&gt; fn);

    // 阻塞线程，等待此次RPC调用完成(或是超时)

    Result get() throws InterruptedException, ExecutionException;

    Result get(long timeout, TimeUnit unit) throws InterruptedException, ExecutionException, TimeoutException;

    // Result中同样可以携带附加信息

    Map&lt;String, String&gt; getAttachments();

    Map&lt;String, Object&gt; getObjectAttachments();

    void addAttachments(Map&lt;String, String&gt; map);

    void addObjectAttachments(Map&lt;String, Object&gt; map);

    void setAttachments(Map&lt;String, String&gt; map);

    void setObjectAttachments(Map&lt;String, Object&gt; map);

    String getAttachment(String key);

    Object getObjectAttachment(String key);

    String getAttachment(String key, String defaultValue);

    Object getObjectAttachment(String key, Object defaultValue);

    void setAttachment(String key, String value);

    void setAttachment(String key, Object value);

    void setObjectAttachment(String key, Object valu

}
</code></pre>
<p>在上面介绍 Provider 端的 Invoker 时提到，我们的业务接口实现会被包装成一个 AbstractProxyInvoker 对象，然后由 Exporter 暴露出去，让 Consumer 可以调用到该服务。Exporter 暴露 Invoker 的实现，说白了，就是让 Provider 能够根据请求的各种信息，找到对应的 Invoker。我们可以维护一个 Map，其中 Key 可以根据请求中的信息构建，Value 为封装相应服务 Bean 的 Exporter 对象，这样就可以实现上述服务发布的要求了。</p>
<p>我们先来看 <strong>Exporter 接口</strong>的定义：</p>
<pre><code>public interface Exporter&lt;T&gt; {

    // 获取底层封装的Invoker对象

    Invoker&lt;T&gt; getInvoker();

    // 取消发布底层的Invoker对象

    void unexport();

}
</code></pre>
<p>为了监听服务发布事件以及取消暴露事件，Dubbo 定义了一个 SPI 扩展接口——<strong>ExporterListener 接口</strong>，其定义如下：</p>
<pre><code>@SPI

public interface ExporterListener {

    // 当有服务发布的时候，会触发该方法

    void exported(Exporter&lt;?&gt; exporter) throws RpcException;

    // 当有服务取消发布的时候，会触发该方法

    void unexported(Exporter&lt;?&gt; exporter);

}
</code></pre>
<p>虽然 ExporterListener 是个扩展接口，但是 Dubbo 本身并没有提供什么有用的扩展实现，我们需要自己提供具体实现监听感兴趣的事情。</p>
<p>相应地，我们可以添加 InvokerListener 监听器，监听 Consumer 引用服务时触发的事件，<strong>InvokerListener 接口</strong>的定义如下：</p>
<pre><code>@SPI

public interface InvokerListener {

    // 当服务引用的时候，会触发该方法

    void referred(Invoker&lt;?&gt; invoker) throws RpcException;

    // 当销毁引用的服务时，会触发该方法

    void destroyed(Invoker&lt;?&gt; invoker);

}
</code></pre>
<p><strong>Protocol 接口</strong>是整个 Dubbo Protocol 层的核心接口之一，其中定义了 export() 和 refer() 两个核心方法，具体定义如下：</p>
<pre><code>@SPI(&quot;dubbo&quot;) // 默认使用DubboProtocol实现

public interface Protocol {

    // 默认端口

    int getDefaultPort();

    // 将一个Invoker暴露出去，export()方法实现需要是幂等的，

    // 即同一个服务暴露多次和暴露一次的效果是相同的

    @Adaptive

    &lt;T&gt; Exporter&lt;T&gt; export(Invoker&lt;T&gt; invoker) throws RpcException;

    // 引用一个Invoker，refer()方法会根据参数返回一个Invoker对象，

    // Consumer端可以通过这个Invoker请求到Provider端的服务

    @Adaptive

    &lt;T&gt; Invoker&lt;T&gt; refer(Class&lt;T&gt; type, URL url) throws RpcException;

    // 销毁export()方法以及refer()方法使用到的Invoker对象，释放

    // 当前Protocol对象底层占用的资源

    void destroy();

    // 返回当前Protocol底层的全部ProtocolServer

    default List&lt;ProtocolServer&gt; getServers() {

        return Collections.emptyList();

    }

}
</code></pre>
<p>在 Protocol 接口的实现中，export() 方法并不是简单地将 Invoker 对象包装成 Exporter 对象返回，其中还涉及代理对象的创建、底层 Server 的启动等操作；refer() 方法除了根据传入的 type 类型以及 URL 参数查询 Invoker 之外，还涉及相关 Client 的创建等操作。</p>
<p>Dubbo 在 Protocol 层专门定义了一个 <strong>ProxyFactory 接口</strong>，作为创建代理对象的工厂。ProxyFactory 接口是一个扩展接口，其中定义了 getProxy() 方法为 Invoker 创建代理对象，还定义了 getInvoker() 方法将代理对象反向封装成 Invoker 对象。</p>
<pre><code>@SPI(&quot;javassist&quot;)

public interface ProxyFactory {

    // 为传入的Invoker对象创建代理对象

    @Adaptive({PROXY_KEY})

    &lt;T&gt; T getProxy(Invoker&lt;T&gt; invoker) throws RpcException;

    @Adaptive({PROXY_KEY})

    &lt;T&gt; T getProxy(Invoker&lt;T&gt; invoker, boolean generic) throws RpcException;

    // 将传入的代理对象封装成Invoker对象，可以暂时理解为getProxy()的逆操作

    @Adaptive({PROXY_KEY})

    &lt;T&gt; Invoker&lt;T&gt; getInvoker(T proxy, Class&lt;T&gt; type, URL url) throws RpcException;

}
</code></pre>
<p>看到 ProxyFactory 上的 @SPI 注解，我们知道其默认实现使用 javassist 来创建代码对象，当然，Dubbo 还提供了其他方式来创建代码，例如 JDK 动态代理。</p>
<p><strong>ProtocolServer 接口</strong>是对前文介绍的 RemotingServer 的一层简单封装，其实现也都非常简单，这里就不再展开。</p>
<p>最后一个要介绍的核心接口是 <strong>Filter 接口</strong>。关于 Filter，相信做过 Java Web 编程的同学们会非常熟悉这个基础概念，Java Web 开发中的 Filter 是用来拦截 HTTP 请求的，Dubbo 中的 Filter 接口功能与之类似，是用来拦截 Dubbo 请求的。</p>
<p>在 Dubbo 的 Filter 接口中，定义了一个 invoke() 方法将请求传递给后续的 Invoker 进行处理（后续的这个 Invoker 对象可能是一个 Filter 封装而成的）。Filter 接口的具体定义如下：</p>
<pre><code>@SPI

public interface Filter {

    // 将请求传给后续的Invoker进行处理

    Result invoke(Invoker&lt;?&gt; invoker, Invocation invocation) throws RpcException;

    interface Listener { // 用于监听响应以及异常

        void onResponse(Result appResponse, Invoker&lt;?&gt; invoker, Invocation invocation);

        void onError(Throwable t, Invoker&lt;?&gt; invoker, Invocation invocation);

    }

}
</code></pre>
<p>Filter 也是一个扩展接口，Dubbo 提供了丰富的 Filter 实现来进行功能扩展，当然我们也可以提供自己的 Filter 实现来扩展 Dubbo 的功能。</p>
<h3>总结</h3>
<p>本课时我们首先介绍了 Dubbo RPC 层在整个 Dubbo 框架中所处的位置，然后说明了 dubbo-rpc-api 层的结构以及其中各个包提供的基本功能。接下来，我们还详细介绍了 Dubbo RPC 层中涉及的核心接口，包括 Invoker、Invocation、Protocol、Result、ProxyFactory、ProtocolServer 等核心接口，以及 ExporterListener、Filter 等扩展类的接口。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="22&#32;&#32;Exchange&#32;层剖析：彻底搞懂&#32;Request-Response&#32;模型（下）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="24&#32;&#32;从&#32;Protocol&#32;起手，看服务暴露和服务引用的全流程（上）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433f65ff9a70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
