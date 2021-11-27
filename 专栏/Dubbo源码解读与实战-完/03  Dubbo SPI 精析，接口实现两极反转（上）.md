<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>03  Dubbo SPI 精析，接口实现两极反转（上）.md</title>
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

                    <a class="current-tab" href="03&#32;&#32;Dubbo&#32;SPI&#32;精析，接口实现两极反转（上）.md">03  Dubbo SPI 精析，接口实现两极反转（上）.md</a>
                    

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
                        <div><h1>03  Dubbo SPI 精析，接口实现两极反转（上）</h1>
<p>Dubbo 为了更好地达到 OCP 原则（即“对扩展开放，对修改封闭”的原则），采用了“<strong>微内核+插件</strong>”的架构。那什么是微内核架构呢？微内核架构也被称为插件化架构（Plug-in Architecture），这是一种面向功能进行拆分的可扩展性架构。内核功能是比较稳定的，只负责管理插件的生命周期，不会因为系统功能的扩展而不断进行修改。功能上的扩展全部封装到插件之中，插件模块是独立存在的模块，包含特定的功能，能拓展内核系统的功能。</p>
<p>微内核架构中，内核通常采用 Factory、IoC、OSGi 等方式管理插件生命周期，<strong>Dubbo 最终决定采用 SPI 机制来加载插件</strong>，Dubbo SPI 参考 JDK 原生的 SPI 机制，进行了性能优化以及功能增强。因此，在讲解 Dubbo SPI 之前，我们有必要先来介绍一下 JDK SPI 的工作原理。</p>
<h3>JDK SPI</h3>
<p>SPI（Service Provider Interface）主要是被<strong>框架开发人员</strong>使用的一种技术。例如，使用 Java 语言访问数据库时我们会使用到 java.sql.Driver 接口，不同数据库产品底层的协议不同，提供的 java.sql.Driver 实现也不同，在开发 java.sql.Driver 接口时，开发人员并不清楚用户最终会使用哪个数据库，在这种情况下就可以使用 Java SPI 机制在实际运行过程中，为 java.sql.Driver 接口寻找具体的实现。</p>
<h4>1. JDK SPI 机制</h4>
<p>当服务的提供者提供了一种接口的实现之后，需要在 Classpath 下的 META-INF/services/ 目录里创建一个以服务接口命名的文件，此文件记录了该 jar 包提供的服务接口的具体实现类。当某个应用引入了该 jar 包且需要使用该服务时，JDK SPI 机制就可以通过查找这个 jar 包的 META-INF/services/ 中的配置文件来获得具体的实现类名，进行实现类的加载和实例化，最终使用该实现类完成业务功能。</p>
<p>下面我们通过一个简单的示例演示下 JDK SPI 的基本使用方式：</p>
<p><img src="assets/CgqCHl8o_UCAI01eAABGsg2cqbw825.png" alt="image" />.png]</p>
<p>首先我们需要创建一个 Log 接口，来模拟日志打印的功能：</p>
<pre><code>public interface Log { 

    void log(String info); 

} 
</code></pre>
<p>接下来提供两个实现—— Logback 和 Log4j，分别代表两个不同日志框架的实现，如下所示：</p>
<pre><code>public class Logback implements Log { 

    @Override 

    public void log(String info) { 

        System.out.println(&quot;Logback:&quot; + info); 

    } 

} 

public class Log4j implements Log { 

    @Override 

    public void log(String info) { 

        System.out.println(&quot;Log4j:&quot; + info); 

    } 

} 
</code></pre>
<p>在项目的 resources/META-INF/services 目录下添加一个名为 com.xxx.Log 的文件，这是 JDK SPI 需要读取的配置文件，具体内容如下：</p>
<pre><code>com.xxx.impl.Log4j 

com.xxx.impl.Logback 
</code></pre>
<p>最后创建 main() 方法，其中会加载上述配置文件，创建全部 Log 接口实现的实例，并执行其 log() 方法，如下所示：</p>
<pre><code>public class Main { 

    public static void main(String[] args) { 

        ServiceLoader&lt;Log&gt; serviceLoader =  

                ServiceLoader.load(Log.class); 

        Iterator&lt;Log&gt; iterator = serviceLoader.iterator(); 

        while (iterator.hasNext()) { 

            Log log = iterator.next(); 

            log.log(&quot;JDK SPI&quot;);  

        } 

    } 

} 

// 输出如下: 

// Log4j:JDK SPI 

// Logback:JDK SPI 
</code></pre>
<h4>2. JDK SPI 源码分析</h4>
<p>通过上述示例，我们可以看到 JDK SPI 的入口方法是 ServiceLoader.load() 方法，接下来我们就对其具体实现进行深入分析。</p>
<p>在 ServiceLoader.load() 方法中，首先会尝试获取当前使用的 ClassLoader（获取当前线程绑定的 ClassLoader，查找失败后使用 SystemClassLoader），然后调用 reload() 方法，调用关系如下图所示：</p>
<p><img src="assets/Ciqc1F8o_V6AR93jAABeDIu_Kso211.png" alt="image" /></p>
<p>在 reload() 方法中，首先会清理 providers 缓存（LinkedHashMap 类型的集合），该缓存用来记录 ServiceLoader 创建的实现对象，其中 Key 为实现类的完整类名，Value 为实现类的对象。之后创建 LazyIterator 迭代器，用于读取 SPI 配置文件并实例化实现类对象。</p>
<p>ServiceLoader.reload() 方法的具体实现，如下所示：</p>
<pre><code>// 缓存，用来缓存 ServiceLoader创建的实现对象 

private LinkedHashMap&lt;String,S&gt; providers = new LinkedHashMap&lt;&gt;(); 

public void reload() { 

    providers.clear(); // 清空缓存 

    lookupIterator = new LazyIterator(service, loader); // 迭代器 

} 
</code></pre>
<p>在前面的示例中，main() 方法中使用的迭代器底层就是调用了 ServiceLoader.LazyIterator 实现的。Iterator 接口有两个关键方法：hasNext() 方法和 next() 方法。这里的 LazyIterator 中的next() 方法最终调用的是其 nextService() 方法，hasNext() 方法最终调用的是 hasNextService() 方法，调用关系如下图所示：</p>
<p><img src="assets/Ciqc1F8o_WmAZSkmAABmcc0uM54214.png" alt="image" /></p>
<p>首先来看 LazyIterator.hasNextService() 方法，该方法主要<strong>负责查找 META-INF/services 目录下的 SPI 配置文件</strong>，并进行遍历，大致实现如下所示：</p>
<pre><code>private static final String PREFIX = &quot;META-INF/services/&quot;; 

Enumeration&lt;URL&gt; configs = null; 

Iterator&lt;String&gt; pending = null; 

String nextName = null; 

private boolean hasNextService() { 

    if (nextName != null) { 

        return true; 

    } 

    if (configs == null) { 

        // PREFIX前缀与服务接口的名称拼接起来，就是META-INF目录下定义的SPI配 

        // 置文件(即示例中的META-INF/services/com.xxx.Log) 

        String fullName = PREFIX + service.getName(); 

        // 加载配置文件 

        if (loader == null) 

            configs = ClassLoader.getSystemResources(fullName); 

        else 

            configs = loader.getResources(fullName); 

    } 

    // 按行SPI遍历配置文件的内容 

    while ((pending == null) || !pending.hasNext()) {  

        if (!configs.hasMoreElements()) { 

            return false; 

        } 

        // 解析配置文件 

        pending = parse(service, configs.nextElement());  

    } 

    nextName = pending.next(); // 更新 nextName字段 

    return true; 

}   
</code></pre>
<p>在 hasNextService() 方法中完成 SPI 配置文件的解析之后，再来看 LazyIterator.nextService() 方法，该方法<strong>负责实例化 hasNextService() 方法读取到的实现类</strong>，其中会将实例化的对象放到 providers 集合中缓存起来，核心实现如下所示：</p>
<pre><code>private S nextService() { 

    String cn = nextName; 

    nextName = null; 

    // 加载 nextName字段指定的类 

    Class&lt;?&gt; c = Class.forName(cn, false, loader); 

    if (!service.isAssignableFrom(c)) { // 检测类型 

        fail(service, &quot;Provider &quot; + cn  + &quot; not a subtype&quot;); 

    } 

    S p = service.cast(c.newInstance()); // 创建实现类的对象 

    providers.put(cn, p); // 将实现类名称以及相应实例对象添加到缓存 

    return p; 

} 
</code></pre>
<p>以上就是在 main() 方法中使用的迭代器的底层实现。最后，我们再来看一下 main() 方法中使用ServiceLoader.iterator() 方法拿到的迭代器是如何实现的，这个迭代器是依赖 LazyIterator 实现的一个匿名内部类，核心实现如下：</p>
<pre><code>public Iterator&lt;S&gt; iterator() { 

    return new Iterator&lt;S&gt;() { 

        // knownProviders用来迭代providers缓存 

        Iterator&lt;Map.Entry&lt;String,S&gt;&gt; knownProviders 

            = providers.entrySet().iterator(); 

        public boolean hasNext() { 

            // 先走查询缓存，缓存查询失败，再通过LazyIterator加载 

            if (knownProviders.hasNext())  

                return true; 

            return lookupIterator.hasNext(); 

        } 

        public S next() { 

            // 先走查询缓存，缓存查询失败，再通过 LazyIterator加载 

            if (knownProviders.hasNext()) 

                return knownProviders.next().getValue(); 

            return lookupIterator.next(); 

        } 

        // 省略remove()方法 

    }; 

} 
</code></pre>
<h4>3. JDK SPI 在 JDBC 中的应用</h4>
<p>了解了 JDK SPI 实现的原理之后，我们再来看实践中 JDBC 是如何使用 JDK SPI 机制加载不同数据库厂商的实现类。</p>
<p>JDK 中只定义了一个 java.sql.Driver 接口，具体的实现是由不同数据库厂商来提供的。这里我们就以 MySQL 提供的 JDBC 实现包为例进行分析。</p>
<p>在 mysql-connector-java-*.jar 包中的 META-INF/services 目录下，有一个 java.sql.Driver 文件中只有一行内容，如下所示：</p>
<pre><code>com.mysql.cj.jdbc.Driver 
</code></pre>
<p>在使用 mysql-connector-java-*.jar 包连接 MySQL 数据库的时候，我们会用到如下语句创建数据库连接：</p>
<pre><code>String url = &quot;jdbc:xxx://xxx:xxx/xxx&quot;; 

Connection conn = DriverManager.getConnection(url, username, pwd); 
</code></pre>
<p><strong>DriverManager 是 JDK 提供的数据库驱动管理器</strong>，其中的代码片段，如下所示：</p>
<pre><code>static { 

    loadInitialDrivers(); 

    println(&quot;JDBC DriverManager initialized&quot;); 

} 
</code></pre>
<p>在调用 getConnection() 方法的时候，DriverManager 类会被 Java 虚拟机加载、解析并触发 static 代码块的执行；在 loadInitialDrivers() 方法中通过 JDK SPI 扫描 Classpath 下 java.sql.Driver 接口实现类并实例化，核心实现如下所示：</p>
<pre><code>private static void loadInitialDrivers() { 

    String drivers = System.getProperty(&quot;jdbc.drivers&quot;) 

    // 使用 JDK SPI机制加载所有 java.sql.Driver实现类 

    ServiceLoader&lt;Driver&gt; loadedDrivers =  

           ServiceLoader.load(Driver.class); 

    Iterator&lt;Driver&gt; driversIterator = loadedDrivers.iterator(); 

    while(driversIterator.hasNext()) { 

        driversIterator.next(); 

    } 

    String[] driversList = drivers.split(&quot;:&quot;); 

    for (String aDriver : driversList) { // 初始化Driver实现类 

        Class.forName(aDriver, true, 

            ClassLoader.getSystemClassLoader()); 

    } 

} 
</code></pre>
<p>在 MySQL 提供的 com.mysql.cj.jdbc.Driver 实现类中，同样有一段 static 静态代码块，这段代码会创建一个 com.mysql.cj.jdbc.Driver 对象并注册到 DriverManager.registeredDrivers 集合中（CopyOnWriteArrayList 类型），如下所示：</p>
<pre><code>static { 

   java.sql.DriverManager.registerDriver(new Driver()); 

} 
</code></pre>
<p>在 getConnection() 方法中，DriverManager 从该 registeredDrivers 集合中获取对应的 Driver 对象创建 Connection，核心实现如下所示：</p>
<pre><code>private static Connection getConnection(String url, java.util.Properties info, Class&lt;?&gt; caller) throws SQLException { 

    // 省略 try/catch代码块以及权限处理逻辑 

    for(DriverInfo aDriver : registeredDrivers) { 

        Connection con = aDriver.driver.connect(url, info); 

        return con; 

    } 

} 
</code></pre>
<h3>总结</h3>
<p>本文我们通过一个示例入手，介绍了 JDK 提供的 SPI 机制的基本使用，然后深入分析了 JDK SPI 的核心原理和底层实现，对其源码进行了深入剖析，最后我们以 MySQL 提供的 JDBC 实现为例，分析了 JDK SPI 在实践中的使用方式。</p>
<p>JDK SPI 机制虽然简单易用，但是也存在一些小瑕疵，你可以先思考一下，在下一课时剖析 Dubbo SPI 机制的时候，我会为你解答该问题。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="02&#32;Dubbo&#32;的配置总线：抓住&#32;URL，就理解了半个&#32;Dubbo.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="04&#32;&#32;Dubbo&#32;SPI&#32;精析，接口实现两极反转（下）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433ee5ec3270ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
