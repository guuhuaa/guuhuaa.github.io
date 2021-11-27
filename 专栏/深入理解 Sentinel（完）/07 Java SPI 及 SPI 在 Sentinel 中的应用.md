<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>07 Java SPI 及 SPI 在 Sentinel 中的应用.md</title>
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

                    
                    <a href="01&#32;开篇词：一次服务雪崩问题排查经历.md">01 开篇词：一次服务雪崩问题排查经历.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;为什么需要服务降级以及常见的几种降级方式.md">02 为什么需要服务降级以及常见的几种降级方式.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;为什么选择&#32;Sentinel，Sentinel&#32;与&#32;Hystrix&#32;的对比.md">03 为什么选择 Sentinel，Sentinel 与 Hystrix 的对比.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;Sentinel&#32;基于滑动窗口的实时指标数据统计.md">04 Sentinel 基于滑动窗口的实时指标数据统计.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;Sentinel&#32;的一些概念与核心类介绍.md">05 Sentinel 的一些概念与核心类介绍.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;Sentinel&#32;中的责任链模式与&#32;Sentinel&#32;的整体工作流程.md">06 Sentinel 中的责任链模式与 Sentinel 的整体工作流程.md</a>

                </li>
                <li>

                    <a class="current-tab" href="07&#32;Java&#32;SPI&#32;及&#32;SPI&#32;在&#32;Sentinel&#32;中的应用.md">07 Java SPI 及 SPI 在 Sentinel 中的应用.md</a>
                    

                </li>
                <li>

                    
                    <a href="08&#32;资源指标数据统计的实现全解析（上）.md">08 资源指标数据统计的实现全解析（上）.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;资源指标数据统计的实现全解析（下）.md">09 资源指标数据统计的实现全解析（下）.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;限流降级与流量效果控制器（上）.md">10 限流降级与流量效果控制器（上）.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;限流降级与流量效果控制器（中）.md">11 限流降级与流量效果控制器（中）.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;限流降级与流量效果控制器（下）.md">12 限流降级与流量效果控制器（下）.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;熔断降级与系统自适应限流.md">13 熔断降级与系统自适应限流.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;黑白名单限流与热点参数限流.md">14 黑白名单限流与热点参数限流.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;自定义&#32;ProcessorSlot&#32;实现开关降级.md">15 自定义 ProcessorSlot 实现开关降级.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;Sentinel&#32;动态数据源：规则动态配置.md">16 Sentinel 动态数据源：规则动态配置.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;Sentinel&#32;主流框架适配.md">17 Sentinel 主流框架适配.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;Sentinel&#32;集群限流的实现（上）.md">18 Sentinel 集群限流的实现（上）.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;Sentinel&#32;集群限流的实现（下）.md">19 Sentinel 集群限流的实现（下）.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;结束语：Sentinel&#32;对应用的性能影响如何？.md">20 结束语：Sentinel 对应用的性能影响如何？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;番外篇：Sentinel&#32;1.8.0&#32;熔断降级新特性解读.md">21 番外篇：Sentinel 1.8.0 熔断降级新特性解读.md</a>

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
                        <div><h1>07 Java SPI 及 SPI 在 Sentinel 中的应用</h1>
<p>SPI 全称是 Service Provider Interface，直译就是服务提供者接口，是一种服务发现机制，是 Java 的一个内置标准，允许不同的开发者去实现某个特定的服务。SPI 的本质是将接口实现类的全限定名配置在文件中，由服务加载器读取配置文件，加载实现类，实现在运行时动态替换接口的实现类。</p>
<p>使用 SPI 机制能够实现按配置加载接口的实现类，SPI 机制在阿里开源的项目中被广泛使用，例如 Dubbo、RocketMQ、以及本文介绍的 Sentinel。RocketMQ 与 Sentinel 使用的都是 Java 提供的 SPI 机制，而 Dubbo 则是使用自实现的一套 SPI，与 Java SPI 的配置方式不同，Dubbo SPI 使用 Key-Value 方式配置，目的是实现自适应扩展机制。</p>
<h3>Java SPI 简介</h3>
<p>我们先来个“Hello Word”级别的 Demo 学习一下 Java SPI 怎么使用，通过这个例子认识 Java SPI。</p>
<p><strong>第一步：定义接口</strong></p>
<p>假设我们有多种登录方式，则创建一个 LoginService 接口。</p>
<pre><code class="language-java">public interface LoginService{
  void login(String username,String password);
}

</code></pre>
<p><strong>第二步：编写接口实现类</strong></p>
<p>假设一开始我们使用 Shiro 框架实现用户鉴权，提供了一个 ShiroLoginService。</p>
<pre><code class="language-java">public class ShiroLoginService implements LoginService{
  public void login(String username,String password){
    // 实现登陆
  }
}

</code></pre>
<p>现在我们不想搞那么麻烦，比如我们可以直接使用 Spring MVC 的拦截器实现用户鉴权，那么可以提供一个 SpringLoginService。</p>
<pre><code class="language-java">public class SpringLoginService implements LoginService{
  public void login(String username,String password){
    // 实现登陆
  }
}

</code></pre>
<p><strong>第三步：通过配置使用 SpringLoginService 或 ShiroLoginService。</strong></p>
<p>当我们想通过修改配置文件的方式而不修改代码实现权限验证框架的切换，就可以使用 Java 的 SPI。通过运行时从配置文件中读取实现类，加载使用配置的实现类。</p>
<p>需要在 resources 目录下新建一个目录 META-INF，并在 META-INF 目录下创建 services 目录，用来存放接口配置文件。</p>
<p>配置文件名为接口 LoginService 全类名，文件中写入使用的实现类的全类名。只要是在 META-INF/services 目录下，只要文件名是接口的全类名，那么编写配置文件内容的时候，IDEA 就会自动提示有哪些实现类。</p>
<p>文件：/resources/META-INF/services/接口名称，填写的内容为接口的实现类，多个实现类使用换行分开。</p>
<pre><code>com.wujiuye.spi.ShiroLoginService

</code></pre>
<p><strong>第四步：编写 main 方法测试使用 Java SPI 加载 LoginService。</strong></p>
<pre><code class="language-java">public class JavaSPI{
  public static void main(String[] args){
    ServiceLoader&lt;LoginService&gt; serviceLoader = ServiceLoader.load(ServiceLoader.class);
    for(LoginService serviceImpl:serviceLoader){
      serviceImpl.login(&quot;wujiuye&quot;,&quot;123456&quot;);
    }
  }
}

</code></pre>
<p>ServiceLoader（服务加载器）是 Java 提供的 SPI 机制的实现，调用 load 方法传入接口名就能获取到一个 ServiceLoader 实例，此时配置文件中注册的实现类是还没有加载到 JVM 的，只有通过 Iterator 遍历获取的时候，才会去加载实现类与实例化实现类。</p>
<p>需要说明的是，例子中配置文件只配置了一个实现类，但其实我们是可以配置 N 多个的，并且 iterator 遍历的顺序就是配置文件中注册实现类的顺序。如果非要想一个注册多实现类的适用场景的话，责任链（拦截器、过滤器）模式这种可插拔的设计模式最适合不过。又或者一个画图程序，定义一个形状接口，实现类可以有矩形、三角形等，如果后期添加了圆形，只需要在形状接口的配置文件中注册圆形就能支持画圆形，完全不用修改任何代码。</p>
<p>ServiceLoader 源码很容易理解，就是根据传入的接口获取接口的全类名，将前缀“/META-INF/services”与接口的全类名拼接定位到配置文件，读取配置文件中的字符串、解析字符串，将解析出来的实现类全类名添加到一个数组，返回一个 ServiceLoader 实例。只有在遍历迭代器的时候 ServiceLoader 才通过调用 Class#forName 方法加载类并且通过反射创建实例，如果不指定类加载器，就使用当前线程的上下文类加载器加载类。</p>
<h3>Java SPI 在 Sentinel 中的应用</h3>
<p>在 sentinel-core 模块的 resources 资源目录下，有一个 META-INF/services 目录，该目录下有两个以接口全名命名的文件，其中 com.alibaba.csp.sentinel.slotchain.SlotChainBuilder 文件用于配置 SlotChainBuilder 接口的实现类，com.alibaba.csp.sentinel.init.InitFunc 文件用于配置 InitFunc 接口的实现类，并且这两个配置文件中都配置了接口的默认实现类，如果我们不添加新的配置，Sentinel 将使用默认配置的接口实现类。</p>
<p>com.alibaba.csp.sentinel.init.InitFunc 文件的默认配置如下：</p>
<pre><code class="language-txt">  com.alibaba.csp.sentinel.metric.extension.MetricCallbackInit

</code></pre>
<p>com.alibaba.csp.sentinel.slotchain.SlotChainBuilder 文件的默认配置如下：</p>
<pre><code class="language-java">  # Default slot chain builder
  com.alibaba.csp.sentinel.slots.DefaultSlotChainBuilder

</code></pre>
<p>ServiceLoader 可加载接口配置文件中配置的所有实现类并且使用反射创建对象，但是否全部加载以及实例化还是由使用者自己决定。Sentinel 的 core 模块使用 Java SPI 机制加载 InitFunc 与 SlotChainBuilder 的实现上稍有不同，如果 InitFunc 接口的配置文件注册了多个实现类，那么这些注册的 InitFunc 实现类都会被 Sentinel 加载、实例化，且都会被使用，但 SlotChainBuilder 不同，如果注册多个实现类，Sentinel 只会加载和使用第一个。</p>
<p>调用 ServiceLoader#load 方法传入接口可获取到一个 ServiceLoader 实例，ServiceLoader 实现了 Iterable 接口，所以可以使用 forEach 语法遍历，ServiceLoader 使用 layz 方式实现迭代器（Iterator），只有被迭代器的 next 方法遍历到的类才会被加载和实例化。如果只想使用接口配置文件中注册的第一个实现类，那么可在使用迭代器遍历时，使用 break 跳出循环。</p>
<p>Sentinel 在加载 SlotChainBuilder 时，只会获取第一个非默认（非 DefaultSlotChainBuilder）实现类的实例，如果接口配置文件中除了默认实现类没有注册别的实现类，则 Sentinel 会使用这个默认的 SlotChainBuilder。其实现源码在 SpiLoader 的 loadFirstInstanceOrDefault 方法中，代码如下。</p>
<pre><code class="language-java">public final class SpiLoader {
    public static &lt;T&gt; T loadFirstInstanceOrDefault(Class&lt;T&gt; clazz, Class&lt;? extends T&gt; defaultClass) {
        try {
            // 缓存的实现省略...
            // 返回第一个类型不等于 defaultClass 的实例
            // ServiceLoader 实现了 Iterable 接口
            for (T instance : serviceLoader) {
                // 获取第一个非默认类的实例
                if (instance.getClass() != defaultClass) {
                    return instance;
                }
            }
            // 没有则使用默认类的实例，反射创建对象
            return defaultClass.newInstance();
        } catch (Throwable t) {
            return null;
        }
    }
}

</code></pre>
<p>Sentinel 加载 InitFunc 则不同，因为 Sentinel 允许存在多个初始化方法。InitFunc 可用于初始化配置限流、熔断规则，但在 Web 项目中我们基本不会使用它，更多的是通过监听 Spring 容器刷新完成事件再去初始化为 Sentinel 配置规则，如果使用动态数据源还可在监听到动态配置改变事件时重新加载规则，所以 InitFunc 我们基本使用不上。</p>
<p>Sentinel 使用 ServiceLoader 加载注册的 InitFunc 实现代码如下：</p>
<pre><code class="language-java">public final class InitExecutor {

    public static void doInit() {
        try {
            // 加载配置
            ServiceLoader&lt;InitFunc&gt; loader = ServiceLoaderUtil.getServiceLoader(InitFunc.class);
            List&lt;OrderWrapper&gt; initList = new ArrayList&lt;OrderWrapper&gt;();
            for (InitFunc initFunc : loader) {
               // 插入数组并排序，同时将 InitFunc 包装为 OrderWrapper
                insertSorted(initList, initFunc);
            }
            // 遍历调用 InitFunc 的初始化方法
            for (OrderWrapper w : initList) {
                w.func.init();
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        } catch (Error error) {
            error.printStackTrace();
        }
    }
}

</code></pre>
<p>虽然 InitFunc 接口与 SlotChainBuilder 接口的配置文件在 sentinel-core 模块下，但我们不需要去修改 Sentinel 的源码，不需要修改 sentinel-core 模块下的接口配置文件，而只需要在当前项目的 /resource/META-INF/services 目录下创建一个与接口全名相同名称的配置文件，并在配置文件中添加接口的实现类即可。项目编译后不会覆盖 sentinel-core 模块下的相同名称的配置文件，而是将两个配置文件合并成一个配置文件。</p>
<h3>自定义 ProcessorSlotChain 构造器</h3>
<p>Sentinel 使用 SlotChainBuilder 将多个 ProcessorSlot 构造成一个 ProcessorSlotChain，由 ProcessorSlotChain 按照 ProcessorSlot 的注册顺序去调用这些 ProcessorSlot。Sentinel 使用 Java SPI 加载 SlotChainBuilder 支持使用者自定义 SlotChainBuilder，相当于是提供了插件的功能。</p>
<p>Sentinel 默认使用的 SlotChainBuilder 是 DefaultSlotChainBuilder，其源码如下：</p>
<pre><code class="language-java">public class DefaultSlotChainBuilder implements SlotChainBuilder {

    @Override
    public ProcessorSlotChain build() {
        ProcessorSlotChain chain = new DefaultProcessorSlotChain();
        chain.addLast(new NodeSelectorSlot());
        chain.addLast(new ClusterBuilderSlot());
        chain.addLast(new LogSlot());
        chain.addLast(new StatisticSlot());
        chain.addLast(new AuthoritySlot());
        chain.addLast(new SystemSlot());
        chain.addLast(new FlowSlot());
        chain.addLast(new DegradeSlot());
        return chain;
    }

}

</code></pre>
<p>DefaultSlotChainBuilder 构造的 ProcessorSlotChain 注册了 NodeSelectorSlot、ClusterBuilderSlot、LogSlot、StatisticSlot、AuthoritySlot、SystemSlot、FlowSlot、DegradeSlot，但这些 ProcessorSlot 并非都是必须的，如果注册的这些 ProcessorSlot 有些我们用不到，那么我们可以自己实现一个 SlotChainBuilder，自己构造 ProcessorSlotChain。例如，我们可以将 LogSlot、AuthoritySlot、SystemSlot 去掉。</p>
<p>第一步，编写 MySlotChainBuilder，实现 SlotChainBuilder 接口，代码如下：</p>
<pre><code class="language-java">public class MySlotChainBuilder implements SlotChainBuilder {

    @Override
    public ProcessorSlotChain build() {
        ProcessorSlotChain chain = new DefaultProcessorSlotChain();
        chain.addLast(new NodeSelectorSlot());
        chain.addLast(new ClusterBuilderSlot());
        chain.addLast(new StatisticSlot());
        chain.addLast(new FlowSlot());
        chain.addLast(new DegradeSlot());
        return chain;
    }

}

</code></pre>
<p>第二步，在当前项目的 /resources/META-INF/services 目录下添加名为 com.alibaba.csp.sentinel.slotchain.SlotChainBuilder 的接口配置文件，并在配置文件中注册 MySlotChainBuilder。</p>
<pre><code class="language-txt">com.wujiuye.sck.provider.config.MySlotChainBuilder

</code></pre>
<p>在构造 ProcessorSlotChain 时，需注意 ProcessorSlot 的注册顺序，例如，NodeSelectorSlot 需作为 ClusterBuilderSlot 的前驱节点，ClusterBuilderSlot 需作为 StatisticSlot 的前驱节点，否则 Sentinel 运行会出现 bug。但你可以将 DegradeSlot 放在 FlowSlot 的前面，这就是我们上一篇说到的 ProcessorSlot 的排序。</p>
<h3>总结</h3>
<p>Sentinel 使用 Java SPI 为我们提供了插件的功能，也类似于 Spring Boot 提供的自动配置类注册功能。我们可以直接替换 Sentinel 提供的默认 SlotChainBuilder，使用自定义的 SlotChainBuilder 自己构造 ProcessorSlotChain，以此实现修改 ProcessorSlot 排序顺序以及增加或移除 ProcessorSlot。在 Sentinel 1.7.2 版本中，Sentinel 支持使用 SPI 注册 ProcessorSlot，并且支持排序。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="06&#32;Sentinel&#32;中的责任链模式与&#32;Sentinel&#32;的整体工作流程.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="08&#32;资源指标数据统计的实现全解析（上）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4359440b65645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3%20Sentinel%EF%BC%88%E5%AE%8C%EF%BC%89/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
