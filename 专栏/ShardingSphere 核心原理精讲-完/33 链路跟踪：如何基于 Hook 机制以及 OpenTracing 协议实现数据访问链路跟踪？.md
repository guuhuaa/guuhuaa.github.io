<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>33 链路跟踪：如何基于 Hook 机制以及 OpenTracing 协议实现数据访问链路跟踪？.md</title>
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

                    
                    <a href="00&#32;如何正确学习一款分库分表开源框架？.md">00 如何正确学习一款分库分表开源框架？.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;从理论到实践：如何让分库分表真正落地？.md">01  从理论到实践：如何让分库分表真正落地？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;顶级项目：ShardingSphere&#32;是一款什么样的&#32;Apache&#32;开源软件？.md">02  顶级项目：ShardingSphere 是一款什么样的 Apache 开源软件？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;规范兼容：JDBC&#32;规范与&#32;ShardingSphere&#32;是什么关系？.md">03  规范兼容：JDBC 规范与 ShardingSphere 是什么关系？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;应用集成：在业务系统中使用&#32;ShardingSphere&#32;的方式有哪些？.md">04  应用集成：在业务系统中使用 ShardingSphere 的方式有哪些？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;配置驱动：ShardingSphere&#32;中的配置体系是如何设计的？.md">05  配置驱动：ShardingSphere 中的配置体系是如何设计的？.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ShardingSphere%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86%E7%B2%BE%E8%AE%B2-%E5%AE%8C/06%20%20%E6%95%B0%E6%8D%AE%E5%88%86%E7%89%87%EF%BC%9A%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%88%86%E5%BA%93%E3%80%81%E5%88%86%E8%A1%A8%E3%80%81%E5%88%86%E5%BA%93+%E5%88%86%E8%A1%A8%E4%BB%A5%E5%8F%8A%E5%BC%BA%E5%88%B6%E8%B7%AF%E7%94%B1%EF%BC%9F%EF%BC%88%E4%B8%8A%EF%BC%89.md">06  数据分片：如何实现分库、分表、分库+分表以及强制路由？（上）.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ShardingSphere%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86%E7%B2%BE%E8%AE%B2-%E5%AE%8C/07%20%20%E6%95%B0%E6%8D%AE%E5%88%86%E7%89%87%EF%BC%9A%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%88%86%E5%BA%93%E3%80%81%E5%88%86%E8%A1%A8%E3%80%81%E5%88%86%E5%BA%93+%E5%88%86%E8%A1%A8%E4%BB%A5%E5%8F%8A%E5%BC%BA%E5%88%B6%E8%B7%AF%E7%94%B1%EF%BC%9F%EF%BC%88%E4%B8%8B%EF%BC%89.md">07  数据分片：如何实现分库、分表、分库+分表以及强制路由？（下）.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ShardingSphere%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86%E7%B2%BE%E8%AE%B2-%E5%AE%8C/08%20%20%E8%AF%BB%E5%86%99%E5%88%86%E7%A6%BB%EF%BC%9A%E5%A6%82%E4%BD%95%E9%9B%86%E6%88%90%E5%88%86%E5%BA%93%E5%88%86%E8%A1%A8+%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%BB%E4%BB%8E%E6%9E%B6%E6%9E%84%EF%BC%9F.md">08  读写分离：如何集成分库分表+数据库主从架构？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;分布式事务：如何使用强一致性事务与柔性事务？.md">09  分布式事务：如何使用强一致性事务与柔性事务？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;数据脱敏：如何确保敏感数据的安全访问？.md">10  数据脱敏：如何确保敏感数据的安全访问？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;编排治理：如何实现分布式环境下的动态配置管理？.md">11  编排治理：如何实现分布式环境下的动态配置管理？.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;从应用到原理：如何高效阅读&#32;ShardingSphere&#32;源码？.md">12  从应用到原理：如何高效阅读 ShardingSphere 源码？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;微内核架构：ShardingSphere&#32;如何实现系统的扩展性？.md">13  微内核架构：ShardingSphere 如何实现系统的扩展性？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;分布式主键：ShardingSphere&#32;中有哪些分布式主键实现方式？.md">14  分布式主键：ShardingSphere 中有哪些分布式主键实现方式？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;解析引擎：SQL&#32;解析流程应该包括哪些核心阶段？（上）.md">15  解析引擎：SQL 解析流程应该包括哪些核心阶段？（上）.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;解析引擎：SQL&#32;解析流程应该包括哪些核心阶段？（下）.md">16  解析引擎：SQL 解析流程应该包括哪些核心阶段？（下）.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;路由引擎：如何理解分片路由核心类&#32;ShardingRouter&#32;的运作机制？.md">17  路由引擎：如何理解分片路由核心类 ShardingRouter 的运作机制？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;路由引擎：如何实现数据访问的分片路由和广播路由？.md">18  路由引擎：如何实现数据访问的分片路由和广播路由？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;路由引擎：如何在路由过程中集成多种路由策略和路由算法？.md">19  路由引擎：如何在路由过程中集成多种路由策略和路由算法？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;改写引擎：如何理解装饰器模式下的&#32;SQL&#32;改写实现机制？.md">20  改写引擎：如何理解装饰器模式下的 SQL 改写实现机制？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;执行引擎：分片环境下&#32;SQL&#32;执行的整体流程应该如何进行抽象？.md">21  执行引擎：分片环境下 SQL 执行的整体流程应该如何进行抽象？.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;执行引擎：如何把握&#32;ShardingSphere&#32;中的&#32;Executor&#32;执行模型？（上）.md">22  执行引擎：如何把握 ShardingSphere 中的 Executor 执行模型？（上）.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;执行引擎：如何把握&#32;ShardingSphere&#32;中的&#32;Executor&#32;执行模型？（下）.md">23  执行引擎：如何把握 ShardingSphere 中的 Executor 执行模型？（下）.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;归并引擎：如何理解数据归并的类型以及简单归并策略的实现过程？.md">24  归并引擎：如何理解数据归并的类型以及简单归并策略的实现过程？.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;归并引擎：如何理解流式归并和内存归并在复杂归并场景下的应用方式？.md">25  归并引擎：如何理解流式归并和内存归并在复杂归并场景下的应用方式？.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;&#32;读写分离：普通主从架构和分片主从架构分别是如何实现的？.md">26  读写分离：普通主从架构和分片主从架构分别是如何实现的？.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;&#32;分布式事务：如何理解&#32;ShardingSphere&#32;中对分布式事务的抽象过程？.md">27  分布式事务：如何理解 ShardingSphere 中对分布式事务的抽象过程？.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;&#32;分布式事务：ShardingSphere&#32;中如何集成强一致性事务和柔性事务支持？（上）.md">28  分布式事务：ShardingSphere 中如何集成强一致性事务和柔性事务支持？（上）.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;&#32;分布式事务：ShardingSphere&#32;中如何集成强一致性事务和柔性事务支持？（下）.md">29  分布式事务：ShardingSphere 中如何集成强一致性事务和柔性事务支持？（下）.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;&#32;数据脱敏：如何基于改写引擎实现低侵入性数据脱敏方案？.md">30  数据脱敏：如何基于改写引擎实现低侵入性数据脱敏方案？.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;配置中心：如何基于配置中心实现配置信息的动态化管理？.md">31 配置中心：如何基于配置中心实现配置信息的动态化管理？.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;注册中心：如何基于注册中心实现数据库访问熔断机制？.md">32 注册中心：如何基于注册中心实现数据库访问熔断机制？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="33&#32;链路跟踪：如何基于&#32;Hook&#32;机制以及&#32;OpenTracing&#32;协议实现数据访问链路跟踪？.md">33 链路跟踪：如何基于 Hook 机制以及 OpenTracing 协议实现数据访问链路跟踪？.md</a>
                    

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ShardingSphere%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86%E7%B2%BE%E8%AE%B2-%E5%AE%8C/34%20%E7%B3%BB%E7%BB%9F%E9%9B%86%E6%88%90%EF%BC%9A%E5%A6%82%E4%BD%95%E5%AE%8C%E6%88%90%20ShardingSphere%20%E5%86%85%E6%A0%B8%E4%B8%8E%20Spring+SpringBoot%20%E7%9A%84%E6%97%A0%E7%BC%9D%E6%95%B4%E5%90%88%EF%BC%9F.md">34 系统集成：如何完成 ShardingSphere 内核与 Spring+SpringBoot 的无缝整合？.md</a>

                </li>
                <li>

                    
                    <a href="35&#32;结语：ShardingSphere&#32;总结及展望.md">35 结语：ShardingSphere 总结及展望.md</a>

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
                        <div><h1>33 链路跟踪：如何基于 Hook 机制以及 OpenTracing 协议实现数据访问链路跟踪？</h1>
<p>今天我们来讨论 ShardingSphere 中关于编排治理的另一个主题，即链路跟踪。在分布式系统开发过程中，链路跟踪是一项基础设施类的功能。作为一款分布式数据库中间件，ShardingSphere 中也内置了简单而完整的链路跟踪机制。</p>
<h3>链路跟踪基本原理和工具</h3>
<p>在介绍具体的实现过程之前，我们有必要先来了解一些关于链路跟踪的理论知识。</p>
<h4>1.链路跟踪基本原理</h4>
<p>分布式环境下的服务跟踪原理上实际上并不复杂，我们首先需要引入两个基本概念，即 TraceId 和 SpanId。</p>
<ul>
<li><strong>TraceId</strong></li>
</ul>
<p>TraceId 即跟踪 Id。在微服务架构中，每个请求生成一个全局的唯一性 Id，通过这个 Id 可以串联起整个调用链，也就是说请求在分布式系统内部流转时，系统需要始终保持传递其唯一性 Id，直到请求返回，这个唯一性 Id 就是 TraceId。</p>
<ul>
<li><strong>SpanId</strong></li>
</ul>
<p>除了 TraceId 外，我们还需要 SpanId，SpanId 一般被称为跨度 Id。当请求到达各个服务组件时，通过 SpanId 来标识它的开始、具体执行过程和结束。对于每个 Span 而言，它必须有开始和结束两个节点，通过记录开始 Span 和结束 Span 的时间戳统计其 Span 的时间延迟。</p>
<p>整个调用过程中每个请求都要透传 TraceId 和 SpanId。每个服务将该次请求附带的 SpanId 作为父 SpanId 进行记录，并且生成自己的 SpanId。一个没有父 SpanId 的 Span 即为根 Span，可以看成调用链入口。所以要查看某次完整的调用只需根据 TraceId 查出所有调用记录，然后通过父 SpanId 和 SpanId 组织起整个调用父子关系。事实上，围绕如何构建 Trace 和 Span 之间统一的关联关系，业界也存在一个通用的链接跟踪协议，这就是 OpenTracing 协议。</p>
<h4>2.OpenTracing 协议和应用方式</h4>
<p>OpenTracing 是一种协议，也使用与上面介绍的类似的术语来表示链路跟踪的过程。通过提供平台无关、厂商无关的 API，OpenTracing 使得开发人员能够方便的添加或更换链路跟踪系统的实现。目前，诸如 Java、Go、Python 等主流开发语言都提供了对 OpenTracing 协议的支持。</p>
<p>我们以 Java 语言为例来介绍 OpenTracing 协议的应用方式，OpenTracing API 中存在相互关联的最重要的对象，也就是 Tracer 和 Span 接口。</p>
<p>对于 Tracer 接口而言，最重要就是如下所示的 buildSpan 方法，该方法用来根据某一个操作创建一个 Span 对象：</p>
<pre><code>SpanBuilder buildSpan(String operationName);
</code></pre>
<p>我们看到上述 buildSpan 方法返回的实际上是一个 SpanBuilder 对象，而 SpanBuilder 中则存在一组 withTag 重载方法，用于为当前 Span 添加一个标签。标签的作用是供用户进行自定义，可以用来检索查询的标记，是一组键值对。withTag 方法的其中一种定义如下所示：</p>
<pre><code>SpanBuilder withTag(String key, String value);
</code></pre>
<p>我们可以为一个 Span 添加多个 Tag，当把 Tag 添加完毕之后，我们就可以调用如下所示的 start 方法来启动这个 Span：</p>
<pre><code>Span start();
</code></pre>
<p>注意这个方法会返回一个 Span 对象，一旦获取了 Span 对象，我们就可以调用该对象中的 finish 方法来结束这个 Span，该方法会为 Span 自动填充结束时间：</p>
<pre><code>void finish();
</code></pre>
<p>基于以上 OpenTracing API 的介绍，在日常开发过程中，我们在业务代码中嵌入链路跟踪的常见实现方法可以用如下所示的代码片段进行抽象：</p>
<pre><code>//从 OpenTracing 规范的实现框架中获取 Tracer 对象

Tracer tracer = new XXXTracer();

//创建一个 Span 并启动

Span span = tracer.buildSpan(&quot;test&quot;).start();

//添加标签到 Span 中

span.setTag(Tags.COMPONENT, &quot;test -application&quot;);

//执行相关业务逻辑

//完成 Span

span.finish();

//可以根据需要获取 Span 中的相关信息

System.out.println(&quot;Operation name = &quot; + span.operationName());

System.out.println(&quot;Start = &quot; + span.startMicros());

System.out.println(&quot;Finish = &quot; + span.finishMicros());
</code></pre>
<p>事实上，ShardingSphere 集成 OpenTracing API 的做法基本与上述方法类似，让我们一起来看一下。</p>
<h3>ShardingSphere 中的链路跟踪</h3>
<p>对于 ShardingSphere 而言，框架本身并不负责如何采集、存储以及展示应用性能监控的相关数据，而是将整个数据分片引擎中最核心的 SQL 解析与 SQL 执行相关信息发送至应用性能监控系统，并交由其处理。</p>
<p>换句话说，ShardingSphere 仅负责产生具有价值的数据，并通过标准协议递交至第三方系统，而不对这些数据做二次处理。</p>
<p>ShardingSphere 使用 OpenTracing API 发送性能追踪数据。支持 OpenTracing 协议的具体产品都可以和 ShardingSphere 自动对接，比如常见的 SkyWalking、Zipkin 和Jaeger。在 ShardingSphere 中，使用这些具体产品的方式只需要在启动时配置 OpenTracing 协议的实现者即可。</p>
<h4>1.通过 ShardingTracer 获取 Tracer 类</h4>
<p>ShardingSphere 中，所有关于链路跟踪的代码都位于 sharding-opentracing 工程中。我们先来看 ShardingTracer 类，该类的 init 方法完成了 OpenTracing 协议实现类的初始化，如下所示：</p>
<pre><code>public static void init() {

         //从环境变量中获取 OpenTracing 协议的实现类配置

        String tracerClassName = System.getProperty(OPENTRACING_TRACER_CLASS_NAME);

        Preconditions.checkNotNull(tracerClassName, &quot;Can not find opentracing tracer implementation class via system property `%s`&quot;, OPENTRACING_TRACER_CLASS_NAME);

        try {

             //初始化 OpenTracing 协议的实现类

            init((Tracer) Class.forName(tracerClassName).newInstance());

        } catch (final ReflectiveOperationException ex) {

            throw new ShardingException(&quot;Initialize opentracing tracer class failure.&quot;, ex);

        }

}
</code></pre>
<p>我们通过配置的 OPENTRACING_TRACER_CLASS_NAME 获取 OpenTracing 协议实现类的类名，然后通过反射创建了实例。例如，我们可以配置该类为如下所示的 Skywalking 框架中的 SkywalkingTracer 类：</p>
<pre><code>org.apache.shardingsphere.opentracing.tracer.class=org.apache.skywalking.apm.toolkit.opentracing.SkywalkingTracer
</code></pre>
<p>当然，ShardingTracer 类也提供了通过直接注入 OpenTracing 协议实现类的方法来进行初始化。实际上上述 init 方法最终也是调用了如下所示的 init 重载方法：</p>
<pre><code>public static void init(final Tracer tracer) {

        if (!GlobalTracer.isRegistered()) {

            GlobalTracer.register(tracer);

        }

}
</code></pre>
<p>该方法把 Tracer 对象存放到全局的 GlobalTracer 中。GlobalTracer 是 OpenTracing API 提供的一个工具类，使用设计模式中的单例模式来存储一个全局性的 Tracer 对象。它的变量定义、register 方法以及 get 方法如下所示：</p>
<pre><code>private static final GlobalTracer INSTANCE = new GlobalTracer();

public static synchronized void register(final Tracer tracer) {

        if (tracer == null) {

            throw new NullPointerException(&quot;Cannot register GlobalTracer &lt;null&gt;.&quot;);

        }

        if (tracer instanceof GlobalTracer) {

            LOGGER.log(Level.FINE, &quot;Attempted to register the GlobalTracer as delegate of itself.&quot;);

            return; // no-op

        }

        if (isRegistered() &amp;&amp; !GlobalTracer.tracer.equals(tracer)) {

            throw new IllegalStateException(&quot;There is already a current global Tracer registered.&quot;);

        }

        GlobalTracer.tracer = tracer;

}

	 

public static Tracer get() {

        return INSTANCE;

}
</code></pre>
<p>采用这种方式，初始化可以采用如下方法：</p>
<pre><code>ShardingTracer.init(new SkywalkingTracer());
</code></pre>
<p>而获取具体 Tracer 对象的方法则直接调用 GlobalTracer 的同名方法即可，如下所示：</p>
<pre><code>public static Tracer get() {

        return GlobalTracer.get();

}
</code></pre>
<h4>2.基于 Hook 机制填充 Span</h4>
<p>一旦获取 Tracer 对象，我们就可以使用该对象来构建各种 Span。ShardingSphere 采用了Hook 机制来填充 Span。说道 Hook 机制，我们可以回想《15 | 解析引擎：SQL 解析流程应该包括哪些核心阶段（上）？》中的相关内容，在如下所示的 SQLParseEngine 类的 parse 方法中用到了 ParseHook：</p>
<pre><code>public SQLStatement parse(final String sql, final boolean useCache) {

	    //基于 Hook 机制进行监控和跟踪

        ParsingHook parsingHook = new SPIParsingHook();

        parsingHook.start(sql);

        try {

           //完成 SQL 的解析，并返回一个 SQLStatement 对象

            SQLStatement result = parse0(sql, useCache);

            parsingHook.finishSuccess(result);

            return result;

        } catch (final Exception ex) {

            parsingHook.finishFailure(ex);

            throw ex;

        }

}
</code></pre>
<p>注意到上述代码中创建了一个 SPIParsingHook，并实现了 ParsingHook 接口，该接口的定义如下所示：</p>
<pre><code>public interface ParsingHook {

    

    //开始 Parse 时进行 Hook

    void start(String sql);

    

    //成功完成 Parse 时进行 Hook

    void finishSuccess(SQLStatement sqlStatement);

    

    //Parse 失败时进行 Hook

    void finishFailure(Exception cause);

}
</code></pre>
<p>SPIParsingHook 实际上是一种容器类，将所有同类型的 Hook 通过 SPI 机制进行实例化并统一调用，SPIParsingHook 的实现方式如下所示：</p>
<pre><code>public final class SPIParsingHook implements ParsingHook {

    

    private final Collection&lt;ParsingHook&gt; parsingHooks = NewInstanceServiceLoader.newServiceInstances(ParsingHook.class);

    

    static {

        NewInstanceServiceLoader.register(ParsingHook.class);

    }

    

    @Override

    public void start(final String sql) {

        for (ParsingHook each : parsingHooks) {

            each.start(sql);

        }

    }

    

    @Override

    public void finishSuccess(final SQLStatement sqlStatement, final ShardingTableMetaData shardingTableMetaData) {

        for (ParsingHook each : parsingHooks) {

            each.finishSuccess(sqlStatement, shardingTableMetaData);

        }

    }

    

    @Override

    public void finishFailure(final Exception cause) {

        for (ParsingHook each : parsingHooks) {

            each.finishFailure(cause);

        }

    }

}
</code></pre>
<p>这里，我们看到了熟悉的 NewInstanceServiceLoader 工具类。这样，我们一旦实现了 ParsingHook，就会在执行 SQLParseEngine 类的 parse 方法时将 Hook 相关的功能嵌入到系统的执行流程中。</p>
<p>另外，OpenTracingParsingHook 同样实现了 ParsingHook 接口，如下所示：</p>
<pre><code>public final class OpenTracingParsingHook implements ParsingHook {

    

    private static final String OPERATION_NAME = &quot;/&quot; + ShardingTags.COMPONENT_NAME + &quot;/parseSQL/&quot;;

    

    private Span span;

    

    @Override

    public void start(final String sql) {

         //创建 Span 并设置 Tag

        span = ShardingTracer.get().buildSpan(OPERATION_NAME)

                .withTag(Tags.COMPONENT.getKey(), ShardingTags.COMPONENT_NAME)

                .withTag(Tags.SPAN_KIND.getKey(), Tags.SPAN_KIND_CLIENT)

                .withTag(Tags.DB_STATEMENT.getKey(), sql).startManual();

    }

    

    @Override

    public void finishSuccess(final SQLStatement sqlStatement) {

         //成功时完成 Span

        span.finish();

    }

    

    @Override

    public void finishFailure(final Exception cause) {

         //失败时完成 Span（

        ShardingErrorSpan.setError(span, cause);

        span.finish();

    }

}
</code></pre>
<p>我们知道 Tracer 类提供了 buildSpan 方法创建自定义的 Span 并可以通过 withTag 方法添加自定义的标签。最后，我们可以通过 finish 方法类关闭这个 Span。在这个方法中，我们看到了这些方法的具体应用场景。</p>
<p>同样，在《21 | 执行引擎：分片环境下 SQL 执行的整体流程应该如何进行抽象？》中，我们在的 SQLExecuteCallback 抽象类的 execute0 方法中也看到了 SQLExecutionHook 的应用场景，SQLExecutionHook 接口的定义如下所示：</p>
<pre><code>public interface SQLExecutionHook {

    

    //开始执行 SQL 时进行 Hook

    void start(String dataSourceName, String sql, List&lt;Object&gt; parameters, DataSourceMetaData dataSourceMetaData, boolean isTrunkThread, Map&lt;String, Object&gt; shardingExecuteDataMap);

    

    //成功完成 SQL 执行时进行 Hook

    void finishSuccess();

    

    //SQL 执行失败时进行 Hook

    void finishFailure(Exception cause);

}
</code></pre>
<p>在 ShardingSphere 中，同样存在一套完整的体系来完成对这个接口的实现，包括与 SPIParsingHook 同样充当容器类的 SPISQLExecutionHook，以及基于 OpenTracing 协议的 OpenTracingSQLExecutionHook，其实现过程与 OpenTracingParsingHook 一致，这里不再做具体展开。</p>
<h3>从源码解析到日常开发</h3>
<p>在今天的内容中，我们可以从 ShardingSphere 的源码中提炼两个可以用于日常开发过程的开发技巧。如果我们需要自己实现一个用于分布式环境下的链路监控和分析系统，那么 OpenTracing 规范以及对应的实现类是你的首选。</p>
<p>基于 OpenTracing 规范，业界存在一大批优秀的工具，例如 SkyWalking、Zipkin 和 Jaeger 等，这些工具都可以很容易的集成到你的业务系统中。</p>
<p>另一方面，我们也看到了 Hook 机制的应用场景和方式。Hook 本质上也是一种回调机制，我们可以根据需要提炼出自身所需的各种 Hook，并通过 SPI 的方式动态加载到系统中，以满足不同场景下的需要，ShardingSphere 为我们如何实现和管理系统中的 Hook 实现类提供了很好的实现参考。</p>
<h3>小结与预告</h3>
<p>今天的内容围绕 ShardingSphere 中的链路跟踪实现过程进行了详细展开。我们发现在 ShardingSphere 中关于链路跟踪的代码并不多，所以为了更好地理解链路跟踪的实现机制，我们也花了一些篇幅介绍了链路跟踪的基本原理，以及背后的 OpenTracing 规范的核心类。</p>
<p>然后，我们发现 ShardingSphere 在业务流程的执行过程中内置了一批 Hook，这些 Hook 能够帮助系统收集各种监控信息，并通过 OpenTracing 规范的各种实现类进行统一管理。</p>
<p>这里给你留一道思考题：ShardingSphere 中如何完成与 OpenTracing 协议的集成？</p>
<p>在下一个课时中，我们将介绍 ShardingSphere 源码解析部分的最后一个主题，即 ShardingSphere 的内核如何与 Spring 框架进行无缝集成以降低开发人员的学习成本。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="32&#32;注册中心：如何基于注册中心实现数据库访问熔断机制？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ShardingSphere%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86%E7%B2%BE%E8%AE%B2-%E5%AE%8C/34%20%E7%B3%BB%E7%BB%9F%E9%9B%86%E6%88%90%EF%BC%9A%E5%A6%82%E4%BD%95%E5%AE%8C%E6%88%90%20ShardingSphere%20%E5%86%85%E6%A0%B8%E4%B8%8E%20Spring+SpringBoot%20%E7%9A%84%E6%97%A0%E7%BC%9D%E6%95%B4%E5%90%88%EF%BC%9F.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434cc8bd6070ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/ShardingSphere%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86%E7%B2%BE%E8%AE%B2-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
