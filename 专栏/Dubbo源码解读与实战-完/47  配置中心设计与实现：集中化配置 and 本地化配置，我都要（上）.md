<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>47  配置中心设计与实现：集中化配置 and 本地化配置，我都要（上）.md</title>
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

                    <a class="current-tab" href="47&#32;&#32;配置中心设计与实现：集中化配置&#32;and&#32;本地化配置，我都要（上）.md">47  配置中心设计与实现：集中化配置 and 本地化配置，我都要（上）.md</a>
                    

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
                        <div><h1>47  配置中心设计与实现：集中化配置 and 本地化配置，我都要（上）</h1>
<p><strong>从 2.7.0 版本开始，Dubbo 正式支持配置中心</strong>，在服务自省架构中也依赖配置中心完成 Service ID 与 Service Name 的映射。配置中心在 Dubbo 中主要承担两个职责：</p>
<ul>
<li>外部化配置；</li>
<li>服务治理，负责服务治理规则的存储与通知。</li>
</ul>
<p><strong>外部化配置目的之一是实现配置的集中式管理。</strong> 目前已经有很多成熟的专业配置管理系统（例如，携程开源的 Apollo、阿里开源的 Nacos 等），Dubbo 配置中心的目的不是再“造一次轮子”，而是保证 Dubbo 能与这些成熟的配置管理系统正常工作。</p>
<p>Dubbo 可以同时支持多种配置来源。在 Dubbo 初始化过程中，会从多个来源获取配置，并按照固定的优先级将这些配置整合起来，实现<strong>高优先级的配置覆盖低优先级配置</strong>的效果。这些配置的汇总结果将会参与形成 URL，以及后续的服务发布和服务引用。</p>
<p>Dubbo 目前支持下面四种配置来源，优先级由 1 到 4 逐级降低：</p>
<ol>
<li>System Properties，即 -D 参数；</li>
<li>外部化配置，也就是本课时要介绍的配置中心；</li>
<li>API 接口、注解、XML 配置等编程方式收到的配置，最终得到 ServiceConfig、ReferenceConfig 等对象；</li>
<li>本地 dubbo.properties 配置文件。</li>
</ol>
<h3>Configuration</h3>
<p><strong>Configuration 接口是 Dubbo 中所有配置的基础接口</strong>，其中定义了根据指定 Key 获取对应配置值的相关方法，如下图所示：</p>
<p><img src="assets/Cip5yF_zz3yABBYdAACqAETTGm0778.png" alt="Drawing 0.png" /></p>
<p>Configuration 接口核心方法</p>
<p>从上图中我们可以看到，Configuration 针对不同的 boolean、int、String 返回值都有对应的 get*() 方法，同时还提供了带有默认值的 get*() 方法。<strong>这些 get<p style="text-align:center">*() 方法底层首先调用 getInternalProperty() 方法获取配置值</strong>，然后调用 convert() 方法将获取到的配置值转换成返回值的类型之后返回。getInternalProperty() 是一个抽象方法，由 Configuration 接口的子类具体实现。</p>
<p>下图展示了 Dubbo 中提供的 Configuration 接口实现，包括：SystemConfiguration、EnvironmentConfiguration、InmemoryConfiguration、PropertiesConfiguration、CompositeConfiguration、ConfigConfigurationAdapter 和 DynamicConfiguration。下面我们将结合具体代码逐个介绍其实现。</p>
<p><img src="assets/Cip5yF_zz6eAMN_oAACEEj9pVjg547.png" alt="Drawing 1.png" /></p>
<p>Configuration 继承关系图</p>
<h4>SystemConfiguration &amp; EnvironmentConfiguration</h4>
<p>SystemConfiguration 是从 Java Properties 配置（也就是 -D 配置参数）中获取相应的配置项，EnvironmentConfiguration 是从使用环境变量中获取相应的配置。两者的 getInternalProperty() 方法实现如下：</p>
<pre><code>public class SystemConfiguration implements Configuration {
    public Object getInternalProperty(String key) {
        return System.getProperty(key); // 读取-D配置参数
    }
}
public class EnvironmentConfiguration implements Configuration {
    public Object getInternalProperty(String key) {
        String value = System.getenv(key);
        if (StringUtils.isEmpty(value)) {
            // 读取环境变量中获取相应的配置
            value = System.getenv(StringUtils.toOSStyleKey(key));
        }
        return value;
    }
}
</code></pre>
<h4>InmemoryConfiguration</h4>
<p>InmemoryConfiguration 会在内存中维护一个 Map&lt;String, String&gt; 集合（store 字段），其 getInternalProperty() 方法的实现就是从 store 集合中获取对应配置值：</p>
<pre><code>public class InmemoryConfiguration implements Configuration {
    private Map&lt;String, String&gt; store = new LinkedHashMap&lt;&gt;();
    @Override
    public Object getInternalProperty(String key) {
        return store.get(key);
    }
    // 省略addProperty()等写入store集合的方法
}
</code></pre>
<h4>PropertiesConfiguration</h4>
<p>PropertiesConfiguration 涉及 OrderedPropertiesProvider，其接口的定义如下：</p>
<pre><code>@SPI
public interface OrderedPropertiesProvider {
    // 用于排序
    int priority();
    // 获取Properties配置
    Properties initProperties();
}
</code></pre>
<p>在 PropertiesConfiguration 的构造方法中，会加载 OrderedPropertiesProvider 接口的全部扩展实现，并按照 priority() 方法进行排序。然后，加载默认的 dubbo.properties.file 配置文件。最后，用 OrderedPropertiesProvider 中提供的配置覆盖 dubbo.properties.file 文件中的配置。PropertiesConfiguration 的构造方法的具体实现如下：</p>
<pre><code>public PropertiesConfiguration() {
    // 获取OrderedPropertiesProvider接口的全部扩展名称
    ExtensionLoader&lt;OrderedPropertiesProvider&gt; propertiesProviderExtensionLoader = ExtensionLoader.getExtensionLoader(OrderedPropertiesProvider.class);
    Set&lt;String&gt; propertiesProviderNames = propertiesProviderExtensionLoader.getSupportedExtensions();
    if (propertiesProviderNames == null || propertiesProviderNames.isEmpty()) {
        return;
    }
    // 加载OrderedPropertiesProvider接口的全部扩展实现
    List&lt;OrderedPropertiesProvider&gt; orderedPropertiesProviders = new ArrayList&lt;&gt;();
    for (String propertiesProviderName : propertiesProviderNames) {
        orderedPropertiesProviders.add(propertiesProviderExtensionLoader.getExtension(propertiesProviderName));
    }
    // 排序OrderedPropertiesProvider接口的扩展实现
    orderedPropertiesProviders.sort((OrderedPropertiesProvider a, OrderedPropertiesProvider b) -&gt; {
        return b.priority() - a.priority();
    });
    // 加载默认的dubbo.properties.file配置文件，加载后的结果记录在ConfigUtils.PROPERTIES这个static字段中
    Properties properties = ConfigUtils.getProperties();
    // 使用OrderedPropertiesProvider扩展实现，按序覆盖dubbo.properties.file配置文件中的默认配置
    for (OrderedPropertiesProvider orderedPropertiesProvider :
            orderedPropertiesProviders) {
        properties.putAll(orderedPropertiesProvider.initProperties());
    }
    // 更新ConfigUtils.PROPERTIES字段
    ConfigUtils.setProperties(properties);
}
</code></pre>
<p>在 PropertiesConfiguration.getInternalProperty() 方法中，直接从 ConfigUtils.PROPERTIES 这个 Properties 中获取覆盖后的配置信息。</p>
<pre><code>public Object getInternalProperty(String key) {
    return ConfigUtils.getProperty(key);
}
</code></pre>
<h4>CompositeConfiguration</h4>
<p>CompositeConfiguration 是一个复合的 Configuration 对象，<strong>其核心就是将多个 Configuration 对象组合起来，对外表现为一个 Configuration 对象</strong>。</p>
<p>CompositeConfiguration 组合的 Configuration 对象都保存在 configList 字段中（LinkedList<code>&lt;Configuration&gt;</code> 集合），CompositeConfiguration 提供了 addConfiguration() 方法用于向 configList 集合中添加 Configuration 对象，如下所示：</p>
<pre><code>public void addConfiguration(Configuration configuration) {
    if (configList.contains(configuration)) {
        return; // 不会重复添加同一个Configuration对象
    }
    this.configList.add(configuration);
}
</code></pre>
<p>在 CompositeConfiguration 中维护了一个 prefix 字段和 id 字段，两者可以作为 Key 的前缀进行查询，在 getProperty() 方法中的相关代码如下：</p>
<pre><code>public Object getProperty(String key, Object defaultValue) {
    Object value = null;
    if (StringUtils.isNotEmpty(prefix)) { // 检查prefix
        if (StringUtils.isNotEmpty(id)) { // 检查id
            // prefix和id都作为前缀，然后拼接key进行查询
            value = getInternalProperty(prefix + id + &quot;.&quot; + key);
        }
        if (value == null) {
            // 只把prefix作为前缀，拼接key进行查询
            value = getInternalProperty(prefix + key);
        }
    } else {
        // 若prefix为空，则直接用key进行查询
        value = getInternalProperty(key);
    }
    return value != null ? value : defaultValue;
}
</code></pre>
<p>在 getInternalProperty() 方法中，会按序遍历 configList 集合中的全部 Configuration 查询对应的 Key，返回第一个成功查询到的 Value 值，如下示例代码：</p>
<pre><code>public Object getInternalProperty(String key) {
    Configuration firstMatchingConfiguration = null;
    for (Configuration config : configList) { // 遍历所有Configuration对象
        try {
            if (config.containsKey(key)) { // 得到第一个包含指定Key的Configuration对象
                firstMatchingConfiguration = config; 
                break;
            }
        } catch (Exception e) {
            logger.error(&quot;...&quot;);
        }
    }
    if (firstMatchingConfiguration != null) { // 通过该Configuration查询Key并返回配置值
        return firstMatchingConfiguration.getProperty(key);
    } else {
        return null;
    }
}
</code></pre>
<h4>ConfigConfigurationAdapter</h4>
<p>Dubbo 通过 AbstractConfig 类来抽象实例对应的配置，如下图所示：</p>
<p><img src="assets/CgqCHl_zz8WAHdY3AAMJFKW_uQE360.png" alt="Drawing 2.png" /></p>
<p>AbstractConfig 继承关系图</p>
<p>这些 AbstractConfig 实现基本都对应一个固定的配置，也定义了配置对应的字段以及 getter/setter() 方法。例如，RegistryConfig 这个实现类就对应了注册中心的相关配置，其中包含了 address、protocol、port、timeout 等一系列与注册中心相关的字段以及对应的 getter/setter() 方法，来接收用户通过 XML、Annotation 或是 API 方式传入的注册中心配置。</p>
<p><strong>ConfigConfigurationAdapter 是 AbstractConfig 与 Configuration 之间的适配器</strong>，它会将 AbstractConfig 对象转换成 Configuration 对象。在 ConfigConfigurationAdapter 的构造方法中会获取 AbstractConfig 对象的全部字段，并转换成一个 Map&lt;String, String&gt; 集合返回，该 Map&lt;String, String&gt; 集合将会被 ConfigConfigurationAdapter 的 metaData 字段引用。相关示例代码如下：</p>
<pre><code>public ConfigConfigurationAdapter(AbstractConfig config) {
    // 获取该AbstractConfig对象中的全部字段与字段值的映射
    Map&lt;String, String&gt; configMetadata = config.getMetaData();
    metaData = new HashMap&lt;&gt;(configMetadata.size());
    // 根据AbstractConfig配置的prefix和id，修改metaData集合中Key的名称
    for (Map.Entry&lt;String, String&gt; entry : configMetadata.entrySet()) {
        String prefix = config.getPrefix().endsWith(&quot;.&quot;) ? config.getPrefix() : config.getPrefix() + &quot;.&quot;;
        String id = StringUtils.isEmpty(config.getId()) ? &quot;&quot; : config.getId() + &quot;.&quot;;
        metaData.put(prefix + id + entry.getKey(), entry.getValue());
    }
}
</code></pre>
<p>在 ConfigConfigurationAdapter 的 getInternalProperty() 方法实现中，直接从 metaData 集合中获取配置值即可，如下所示：</p>
<pre><code>public Object getInternalProperty(String key) {
    return metaData.get(key);
}
</code></pre>
<h3>DynamicConfiguration</h3>
<p>DynamicConfiguration 是对 Dubbo 中动态配置的抽象，其核心方法有下面三类。</p>
<ul>
<li>getProperties()/ getConfig() / getProperty() 方法：从配置中心获取指定的配置，在使用时，可以指定一个超时时间。</li>
<li>addListener()/ removeListener() 方法：添加或删除对指定配置的监听器。</li>
<li>publishConfig() 方法：发布一条配置信息。</li>
</ul>
<p>在上述三类方法中，每个方法都用多个重载，其中，都会包含一个带有 group 参数的重载，也就是说<strong>配置中心的配置可以按照 group 进行分组</strong>。</p>
<p>与 Dubbo 中很多接口类似，DynamicConfiguration 接口本身不被 @SPI 注解修饰（即不是一个扩展接口），<strong>而是在 DynamicConfigurationFactory 上添加了 @SPI 注解，使其成为一个扩展接口</strong>。</p>
<p>在 DynamicConfiguration 中提供了 getDynamicConfiguration() 静态方法，该方法会从传入的配置中心 URL 参数中，解析出协议类型并获取对应的 DynamicConfigurationFactory 实现，如下所示：</p>
<pre><code>static DynamicConfiguration getDynamicConfiguration(URL connectionURL) {
    String protocol = connectionURL.getProtocol();
    DynamicConfigurationFactory factory = getDynamicConfigurationFactory(protocol);
    return factory.getDynamicConfiguration(connectionURL);
}
</code></pre>
<p>DynamicConfigurationFactory 接口的定义如下：</p>
<pre><code>@SPI(&quot;nop&quot;) 
public interface DynamicConfigurationFactory {
    DynamicConfiguration getDynamicConfiguration(URL url);
    static DynamicConfigurationFactory getDynamicConfigurationFactory(String name) {
        // 根据扩展名称获取DynamicConfigurationFactory实现
        Class&lt;DynamicConfigurationFactory&gt; factoryClass = DynamicConfigurationFactory.class;
        ExtensionLoader&lt;DynamicConfigurationFactory&gt; loader = getExtensionLoader(factoryClass);
        return loader.getOrDefaultExtension(name);
    }
}
</code></pre>
<p>DynamicConfigurationFactory 接口的继承关系以及 DynamicConfiguration 接口对应的继承关系如下：</p>
<p><img src="assets/CgqCHl_0L-GAPVy9AAEqog2bl7U068.png" alt="11.png" /></p>
<p>DynamicConfigurationFactory 继承关系图</p>
<p><img src="assets/Cip5yF_zz9iAM1YYAAB_QXlLDcU550.png" alt="Drawing 4.png" /></p>
<p>DynamicConfiguration 继承关系图</p>
<p>我们先来看 AbstractDynamicConfigurationFactory 的实现，其中会维护一个 dynamicConfigurations 集合（Map&lt;String, DynamicConfiguration&gt; 类型），在 getDynamicConfiguration() 方法中会填充该集合，实现<strong>缓存</strong>DynamicConfiguration 对象的效果。同时，AbstractDynamicConfigurationFactory 提供了一个 createDynamicConfiguration() 方法给子类实现，来<strong>创建</strong>DynamicConfiguration 对象。</p>
<p>以 ZookeeperDynamicConfigurationFactory 实现为例，其 createDynamicConfiguration() 方法创建的就是 ZookeeperDynamicConfiguration 对象：</p>
<pre><code>protected DynamicConfiguration createDynamicConfiguration(URL url) {
    // 这里创建ZookeeperDynamicConfiguration使用的ZookeeperTransporter就是前文在Transport层中针对Zookeeper的实现
    return new ZookeeperDynamicConfiguration(url, zookeeperTransporter);
}
</code></pre>
<p>接下来我们再以 ZookeeperDynamicConfiguration 为例，分析 DynamicConfiguration 接口的具体实现。</p>
<p>首先来看 ZookeeperDynamicConfiguration 的核心字段。</p>
<ul>
<li>executor（Executor 类型）：用于执行监听器的线程池。</li>
<li>rootPath（String 类型）：以 Zookeeper 作为配置中心时，配置也是以 ZNode 形式存储的，rootPath 记录了所有配置节点的根路径。</li>
<li>zkClient（ZookeeperClient 类型）：与 Zookeeper 集群交互的客户端。</li>
<li>initializedLatch（CountDownLatch 类型）：阻塞等待 ZookeeperDynamicConfiguration 相关的监听器注册完成。</li>
<li>cacheListener（CacheListener 类型）：用于监听配置变化的监听器。</li>
<li>url（URL 类型）：配置中心对应的 URL 对象。</li>
</ul>
<p>在 ZookeeperDynamicConfiguration 的构造函数中，会<strong>初始化上述核心字段</strong>，具体实现如下：</p>
<pre><code>ZookeeperDynamicConfiguration(URL url, ZookeeperTransporter zookeeperTransporter) {
    this.url = url;
    // 根据URL中的config.namespace参数(默认值为dubbo)，确定配置中心ZNode的根路径
    rootPath = PATH_SEPARATOR + url.getParameter(CONFIG_NAMESPACE_KEY, DEFAULT_GROUP) + &quot;/config&quot;;
    // 初始化initializedLatch以及cacheListener，
    // 在cacheListener注册成功之后，会调用cacheListener.countDown()方法
    initializedLatch = new CountDownLatch(1);
    this.cacheListener = new CacheListener(rootPath, initializedLatch);
    // 初始化executor字段，用于执行监听器的逻辑
    this.executor = Executors.newFixedThreadPool(1, new NamedThreadFactory(this.getClass().getSimpleName(), true));
    // 初始化Zookeeper客户端
    zkClient = zookeeperTransporter.connect(url);
    // 在rootPath上添加cacheListener监听器
    zkClient.addDataListener(rootPath, cacheListener, executor);
    try {
        // 从URL中获取当前线程阻塞等待Zookeeper监听器注册成功的时长上限
        long timeout = url.getParameter(&quot;init.timeout&quot;, 5000);
        // 阻塞当前线程，等待监听器注册完成
        boolean isCountDown = this.initializedLatch.await(timeout, TimeUnit.MILLISECONDS);
        if (!isCountDown) {
            throw new IllegalStateException(&quot;...&quot;);
        }
    } catch (InterruptedException e) {
        logger.warn(&quot;...&quot;);
    }
}
</code></pre>
<p>在上述初始化过程中，ZookeeperDynamicConfiguration 会创建 CacheListener 监听器。在前面[第 15 课时]中，我们介绍了 dubbo-remoting-zookeeper 对外提供了 StateListener、DataListener 和 ChildListener 三种类型的监听器。<strong>这里的 CacheListener 就是 DataListener 监听器的具体实现</strong>。</p>
<p>在 CacheListener 中维护了一个 Map&lt;String, Set&gt; 集合（keyListeners 字段）用于记录所有添加的 ConfigurationListener 监听器，其中 Key 是配置信息在 Zookeeper 中存储的 path，Value 为该 path 上的监听器集合。当某个配置项发生变化的时候，CacheListener 会从 keyListeners 中获取该配置对应的 ConfigurationListener 监听器集合，并逐个进行通知。该逻辑是在 CacheListener 的 dataChanged() 方法中实现的：</p>
<pre><code>public void dataChanged(String path, Object value, EventType eventType) {
    if (eventType == null) {
        return;
    }
    if (eventType == EventType.INITIALIZED) {
        // 在收到INITIALIZED事件的时候，表示CacheListener已经成功注册，会释放阻塞在initializedLatch上的主线程
        initializedLatch.countDown();
        return;
    }
    if (path == null || (value == null &amp;&amp; eventType != EventType.NodeDeleted)) {
        return;
    }

    if (path.split(&quot;/&quot;).length &gt;= MIN_PATH_DEPTH) { // 对path层数进行过滤
        String key = pathToKey(path); // 将path中的&quot;/&quot;替换成&quot;.&quot;
        ConfigChangeType changeType;
        switch (eventType) { // 将Zookeeper中不同的事件转换成不同的ConfigChangedEvent事件
            case NodeCreated:
                changeType = ConfigChangeType.ADDED;
                break;
            case NodeDeleted:
                changeType = ConfigChangeType.DELETED;
                break;
            case NodeDataChanged:
                changeType = ConfigChangeType.MODIFIED;
                break;
            default:
                return;
        }
        // 使用ConfigChangedEvent封装触发事件的Key、Value、配置group以及事件类型
        ConfigChangedEvent configChangeEvent = new ConfigChangedEvent(key, getGroup(path), (String) value, changeType);
        // 从keyListeners集合中获取对应的ConfigurationListener集合，然后逐一进行通知
        Set&lt;ConfigurationListener&gt; listeners = keyListeners.get(path);
        if (CollectionUtils.isNotEmpty(listeners)) {
            listeners.forEach(listener -&gt; listener.process(configChangeEvent));
        }
    }
}
</code></pre>
<p>CacheListener 中调用的监听器都是 ConfigurationListener 接口实现，如下图所示，这里涉及[第 33 课时]介绍的 TagRouter、AppRouter 和 ServiceRouter，它们主要是监听路由配置的变化；还涉及 RegistryDirectory 和 RegistryProtocol 中的四个内部类（AbstractConfiguratorListener 的子类），它们主要监听 Provider 和 Consumer 的配置变化。</p>
<p><img src="assets/CgqCHl_0L9WAYbfVAAGH_E-l-UU432.png" alt="222.png" /></p>
<p>ConfigurationListener 继承关系图</p>
<p>这些 ConfigurationListener 实现在前面的课程中已经详细介绍过了，这里就不再重复。ZookeeperDynamicConfiguration 中还提供了 addListener()、removeListener() 两个方法用来增删 ConfigurationListener 监听器，具体实现比较简单，这里就不再展示，你若感兴趣的话可以参考<a href="https://github.com/xxxlxy2008/dubbo">源码</a>进行学习。</p>
<p>介绍完 ZookeeperDynamicConfiguration 的初始化过程之后，我们再来看 ZookeeperDynamicConfiguration 中<strong>读取配置、写入配置</strong>的相关操作。相关方法的实现如下：</p>
<pre><code>public Object getInternalProperty(String key) {
    // 直接从Zookeeper中读取对应的Key
    return zkClient.getContent(key);
}
public boolean publishConfig(String key, String group, String content) {
    // getPathKey()方法中会添加rootPath和group两部分信息到Key中
    String path = getPathKey(group, key);
    // 在Zookeeper中创建对应ZNode节点用来存储配置信息
    zkClient.create(path, content, false);
    return true;
}
</code></pre>
<h3>总结</h3>
<p>本课时我们重点介绍了 Dubbo 配置中心中的多种配置接口。首先，我们讲解了 Configuration 这个顶层接口的核心方法，然后介绍了 Configuration 接口的相关实现，这些实现可以从环境变量、-D 启动参数、Properties文件以及其他配置文件或注解处读取配置信息。最后，我们还着重介绍了 DynamicConfiguration 这个动态配置接口的定义，并分析了以 Zookeeper 为动态配置中心的 ZookeeperDynamicConfiguration 实现。</p>
<p>下一课时，我们将深入介绍 Dubbo 动态配置中心启动的核心流程，记得按时来听课。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="46&#32;&#32;加餐：深入服务自省方案中的服务发布订阅（下）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="48&#32;&#32;配置中心设计与实现：集中化配置&#32;and&#32;本地化配置，我都要（下）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433ff84c7c70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
