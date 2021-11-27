<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>39  加餐：多个返回值不用怕，Merger 合并器来帮忙.md</title>
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

                    <a class="current-tab" href="39&#32;&#32;加餐：多个返回值不用怕，Merger&#32;合并器来帮忙.md">39  加餐：多个返回值不用怕，Merger 合并器来帮忙.md</a>
                    

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
                        <div><h1>39  加餐：多个返回值不用怕，Merger 合并器来帮忙</h1>
<p>你好，我是杨四正，今天我和你分享的主题是 Merger 合并器。</p>
<p>在上一课时中，我们分析 MergeableClusterInvoker 的具体实现时讲解过这样的内容：MergeableClusterInvoker 中会读取 URL 中的 merger 参数值，如果 merger 参数以 &quot;.&quot; 开头，则表示 &quot;.&quot; 后的内容是一个方法名，这个方法名是远程目标方法的返回类型中的一个方法，MergeableClusterInvoker 在拿到所有 Invoker 返回的结果对象之后，会遍历每个返回结果，并调用 merger 参数指定的方法，合并这些结果值。</p>
<p>其实，除了上述指定 Merger 方法名称的合并方式之外，Dubbo 内部还提供了很多默认的 Merger 实现，这也就是本课时将要分析的内容。本课时将详细介绍 MergerFactory 工厂类、Merger 接口以及针对 Java 中常见数据类型的 Merger 实现。</p>
<h3>MergerFactory</h3>
<p>在 MergeableClusterInvoker 使用默认 Merger 实现的时候，会<strong>通过 MergerFactory 以及服务接口返回值类型（returnType），选择合适的 Merger 实现</strong>。</p>
<p>在 MergerFactory 中维护了一个 ConcurrentHashMap 集合（即 MERGER_CACHE 字段），用来缓存服务接口返回值类型与 Merger 实例之间的映射关系。</p>
<p>MergerFactory.getMerger() 方法会根据传入的 returnType 类型，从 MERGER_CACHE 缓存中查找相应的 Merger 实现，下面我们来看该方法的具体实现：</p>
<pre><code>public static &lt;T&gt; Merger&lt;T&gt; getMerger(Class&lt;T&gt; returnType) {

    if (returnType == null) { // returnType为空，直接抛出异常

        throw new IllegalArgumentException(&quot;returnType is null&quot;);

    }

    Merger result;

    if (returnType.isArray()) { // returnType为数组类型

        // 获取数组中元素的类型

        Class type = returnType.getComponentType();

        // 获取元素类型对应的Merger实现

        result = MERGER_CACHE.get(type);

        if (result == null) {

            loadMergers();

            result = MERGER_CACHE.get(type);

        }

        // 如果Dubbo没有提供元素类型对应的Merger实现，则返回ArrayMerger

        if (result == null &amp;&amp; !type.isPrimitive()) {

            result = ArrayMerger.INSTANCE;

        }

    } else {

        // 如果returnType不是数组类型，则直接从MERGER_CACHE缓存查找对应的Merger实例

        result = MERGER_CACHE.get(returnType);

        if (result == null) {

            loadMergers();

            result = MERGER_CACHE.get(returnType);

        }

    }

    return result;

}
</code></pre>
<p>loadMergers() 方法会通过 Dubbo SPI 方式加载 Merger 接口全部扩展实现的名称，并填充到 MERGER_CACHE 集合中，具体实现如下：</p>
<pre><code>static void loadMergers() {

    // 获取Merger接口的所有扩展名称

    Set&lt;String&gt; names = ExtensionLoader.getExtensionLoader(Merger.class)

            .getSupportedExtensions();

    for (String name : names) { // 遍历所有Merger扩展实现

        Merger m = ExtensionLoader.getExtensionLoader(Merger.class).getExtension(name);

        // 将Merger实例与对应returnType的映射关系记录到MERGER_CACHE集合中

        MERGER_CACHE.putIfAbsent(ReflectUtils.getGenericClass(m.getClass()), m);

    }

}
</code></pre>
<h3>ArrayMerger</h3>
<p>在 Dubbo 中提供了处理不同类型返回值的 Merger 实现，其中不仅有处理 boolean[]、byte[]、char[]、double[]、float[]、int[]、long[]、short[] 等<strong>基础类型数组</strong>的 Merger 实现，还有处理 List、Set、Map 等<strong>集合类</strong>的 Merger 实现，具体继承关系如下图所示：</p>
<p><img src="assets/CgqCHl_PFWiAbmfPAAPxSnmLN4s499.png" alt="Lark20201208-135542.png" /></p>
<p>Merger 继承关系图</p>
<p>我们首先来看 ArrayMerger 实现：<strong>当服务接口的返回值为数组的时候，会使用 ArrayMerger 将多个数组合并成一个数组，也就是将二维数组拍平成一维数组</strong>。ArrayMerger.merge() 方法的具体实现如下：</p>
<pre><code>public Object[] merge(Object[]... items) {

    if (ArrayUtils.isEmpty(items)) {

        // 传入的结果集合为空，则直接返回空数组

        return new Object[0];

    }

    int i = 0;

    // 查找第一个不为null的结果

    while (i &lt; items.length &amp;&amp; items[i] == null) {

        i++;

    }

    // 所有items数组中全部结果都为null，则直接返回空数组

    if (i == items.length) {

        return new Object[0];

    }

    Class&lt;?&gt; type = items[i].getClass().getComponentType();

    int totalLen = 0;

    for (; i &lt; items.length; i++) {

        if (items[i] == null) { // 忽略为null的结果

            continue;

        }

        Class&lt;?&gt; itemType = items[i].getClass().getComponentType();

        if (itemType != type) { // 保证类型相同

            throw new IllegalArgumentException(&quot;Arguments' types are different&quot;);

        }

        totalLen += items[i].length;

    }

    if (totalLen == 0) { // 确定最终数组的长度

        return new Object[0];

    }

    Object result = Array.newInstance(type, totalLen);

    int index = 0;

    // 遍历全部的结果数组，将items二维数组中的每个元素都加到result中，形成一维数组

    for (Object[] array : items) {

        if (array != null) {

            for (int j = 0; j &lt; array.length; j++) {

                Array.set(result, index++, array[j]);

            }

        }

    }

    return (Object[]) result;

}
</code></pre>
<p>其他基础数据类型数组的 Merger 实现，与 ArrayMerger 的实现非常类似，都是将相应类型的二维数组拍平成同类型的一维数组，这里以 IntArrayMerger 为例进行分析：</p>
<pre><code>public int[] merge(int[]... items) {

    if (ArrayUtils.isEmpty(items)) {

        // 检测传入的多个int[]不能为空

        return new int[0];

    }

    // 直接使用Stream的API将多个int[]数组拍平成一个int[]数组

    return Arrays.stream(items).filter(Objects::nonNull)

            .flatMapToInt(Arrays::stream)

            .toArray();

}
</code></pre>
<p>剩余的其他基础类型的 Merger 实现类，例如，FloatArrayMerger、IntArrayMerger、LongArrayMerger、BooleanArrayMerger、ByteArrayMerger、CharArrayMerger、DoubleArrayMerger 等，这里就不再赘述，你若感兴趣的话可以参考<a href="https://github.com/xxxlxy2008/dubbo">源码</a>进行学习。</p>
<h3>MapMerger</h3>
<p>SetMerger、ListMerger 和 MapMerger 是针对 Set 、List 和 Map 返回值的 Merger 实现，它们会<strong>将多个 Set（或 List、Map）集合合并成一个 Set（或 List、Map）集合</strong>，核心原理与 ArrayMerger 的实现类似。这里我们先来看 MapMerger 的核心实现：</p>
<pre><code>public Map&lt;?, ?&gt; merge(Map&lt;?, ?&gt;... items) {

    if (ArrayUtils.isEmpty(items)) {

        // 空结果集时，这就返回空Map

        return Collections.emptyMap();

    }

    // 将items中所有Map集合中的KV，添加到result这一个Map集合中

    Map&lt;Object, Object&gt; result = new HashMap&lt;Object, Object&gt;();

    Stream.of(items).filter(Objects::nonNull).forEach(result::putAll);

    return result;

}
</code></pre>
<p>接下来再看 SetMerger 和 ListMerger 的核心实现：</p>
<pre><code>public Set&lt;Object&gt; merge(Set&lt;?&gt;... items) {

    if (ArrayUtils.isEmpty(items)) {

        // 空结果集时，这就返回空Set集合

        return Collections.emptySet();

    }

    // 创建一个新的HashSet集合，传入的所有Set集合都添加到result中

    Set&lt;Object&gt; result = new HashSet&lt;Object&gt;();

    Stream.of(items).filter(Objects::nonNull).forEach(result::addAll);

    return result;

}

public List&lt;Object&gt; merge(List&lt;?&gt;... items) {

    if (ArrayUtils.isEmpty(items)) {

        // 空结果集时，这就返回空Set集合

        return Collections.emptyList();

    }

    // 通过Stream API将传入的所有List集合拍平成一个List集合并返回

    return Stream.of(items).filter(Objects::nonNull)

            .flatMap(Collection::stream)

            .collect(Collectors.toList());

}
</code></pre>
<h3>自定义 Merger 扩展实现</h3>
<p>介绍完 Dubbo 自带的 Merger 实现之后，下面我们还可以尝试动手写一个自己的 Merger 实现，这里我们以 dubbo-demo-xml 中的 Provider 和 Consumer 为例进行修改。</p>
<p>首先我们在 dubbo-demo-xml-provider 示例模块中<strong>发布两个服务</strong>，分别属于 groupA 和 groupB，相应的 dubbo-provider.xml 配置如下：</p>
<pre><code>&lt;beans xmlns:xsi=&quot;http://www.w3.org/2001/XMLSchema-instance&quot;

       xmlns:dubbo=&quot;http://dubbo.apache.org/schema/dubbo&quot;

       xmlns=&quot;http://www.springframework.org/schema/beans&quot;

       xsi:schemaLocation=&quot;http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-4.3.xsd

       http://dubbo.apache.org/schema/dubbo http://dubbo.apache.org/schema/dubbo/dubbo.xsd&quot;&gt;

    &lt;dubbo:application metadata-type=&quot;remote&quot; name=&quot;demo-provider&quot;/&gt;

    &lt;dubbo:metadata-report address=&quot;zookeeper://127.0.0.1:2181&quot;/&gt;

    &lt;dubbo:registry address=&quot;zookeeper://127.0.0.1:2181&quot;/&gt;

    &lt;dubbo:protocol name=&quot;dubbo&quot;/&gt;

    &lt;!-- 配置两个Spring Bean --&gt;

    &lt;bean id=&quot;demoService&quot; class=&quot;org.apache.dubbo.demo.provider.DemoServiceImpl&quot;/&gt;

    &lt;bean id=&quot;demoServiceB&quot; class=&quot;org.apache.dubbo.demo.provider.DemoServiceImpl&quot;/&gt;

    &lt;!-- 将demoService和demoServiceB两个Spring Bean作为服务发布出去，分别属于groupA和groupB--&gt;

    &lt;dubbo:service interface=&quot;org.apache.dubbo.demo.DemoService&quot; ref=&quot;demoService&quot; group=&quot;groupA&quot;/&gt;

    &lt;dubbo:service interface=&quot;org.apache.dubbo.demo.DemoService&quot; ref=&quot;demoServiceB&quot; group=&quot;groupB&quot;/&gt;

&lt;/beans&gt;
</code></pre>
<p>接下来，在 dubbo-demo-xml-consumer 示例模块中<strong>进行服务引用</strong>，dubbo-consumer.xml 配置文件的具体内容如下：</p>
<pre><code>&lt;beans xmlns:xsi=&quot;http://www.w3.org/2001/XMLSchema-instance&quot;

       xmlns:dubbo=&quot;http://dubbo.apache.org/schema/dubbo&quot;

       xmlns=&quot;http://www.springframework.org/schema/beans&quot;

       xsi:schemaLocation=&quot;http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-4.3.xsd

       http://dubbo.apache.org/schema/dubbo http://dubbo.apache.org/schema/dubbo/dubbo.xsd&quot;&gt;

    &lt;dubbo:application name=&quot;demo-consumer&quot;/&gt;

    &lt;dubbo:registry address=&quot;zookeeper://127.0.0.1:2181&quot;/&gt;

    &lt;!-- 引用DemoService，这里指定了group为*，即可以引用任何group的Provider，同时merger设置为true，即需要对结果进行合并--&gt;

    &lt;dubbo:reference id=&quot;demoService&quot; check=&quot;false&quot; interface=&quot;org.apache.dubbo.demo.DemoService&quot; group=&quot;*&quot; merger=&quot;true&quot;/&gt;

&lt;/beans&gt;
</code></pre>
<p>然后，在 dubbo-demo-xml-consumer 示例模块的 /resources/META-INF/dubbo 目录下，添加一个名为 org.apache.dubbo.rpc.cluster.Merger 的 Dubbo SPI 配置文件，其内容如下：</p>
<pre><code>String=org.apache.dubbo.demo.consumer.StringMerger
</code></pre>
<p>StringMerger 实现了前面介绍的 Merger 接口，它<strong>会将多个 Provider 节点返回的 String 结果值拼接起来</strong>，具体实现如下：</p>
<pre><code>public class StringMerger implements Merger&lt;String&gt; {

    @Override

    public String merge(String... items) {

        if (ArrayUtils.isEmpty(items)) { // 检测空返回值

            return &quot;&quot;;

        }

        String result = &quot;&quot;;

        for (String item : items) { // 通过竖线将多个Provider的返回值拼接起来

            result += item + &quot;|&quot;;

        }

        return result;

    }

}
</code></pre>
<p>最后，我们依次启动 Zookeeper、dubbo-demo-xml-provider 示例模块和 dubbo-demo-xml-consumer 示例模块。在控制台中我们会看到如下输出：</p>
<pre><code>result: Hello world, response from provider: 172.17.108.179:20880|Hello world, response from provider: 172.17.108.179:20880|
</code></pre>
<h3>总结</h3>
<p>本课时我们重点介绍了 MergeableCluster 中涉及的 Merger 合并器相关的知识点。</p>
<ul>
<li>首先，我们介绍了 MergerFactory 工厂类的核心功能，它可以配合远程方法调用的返回值，选择对应的 Merger 实现，完成结果的合并。</li>
<li>然后，我们深入分析了 Dubbo 自带的 Merger 实现类，涉及 Java 中各个基础类型数组的 Merger 合并器实现，例如，IntArrayMerger、LongArrayMerger 等，它们都是将多个特定类型的一维数组拍平成相同类型的一维数组。</li>
<li>除了这些基础类型数组的 Merger 实现，Dubbo 还提供了 List、Set、Map 等集合类的 Merger 实现，它们的核心是将多个集合中的元素整理到一个同类型的集合中。</li>
<li>最后，我们还以 StringMerger 为例，介绍了如何自定义 Merger 合并器。</li>
</ul>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="38&#32;&#32;集群容错：一个好汉三个帮（下）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="40&#32;&#32;加餐：模拟远程调用，Mock&#32;机制帮你搞定.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433fc4bb9f70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
