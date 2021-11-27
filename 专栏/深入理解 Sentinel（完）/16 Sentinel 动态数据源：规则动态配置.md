<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>16 Sentinel 动态数据源：规则动态配置.md</title>
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

                    
                    <a href="07&#32;Java&#32;SPI&#32;及&#32;SPI&#32;在&#32;Sentinel&#32;中的应用.md">07 Java SPI 及 SPI 在 Sentinel 中的应用.md</a>

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

                    <a class="current-tab" href="16&#32;Sentinel&#32;动态数据源：规则动态配置.md">16 Sentinel 动态数据源：规则动态配置.md</a>
                    

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
                        <div><h1>16 Sentinel 动态数据源：规则动态配置</h1>
<p>经过前面的学习，我们知道，为资源配置各种规则可使用 Sentinel 提供的各种规则对应的 loadRules API，但这种以编码的方式配置规则很难实现动态修改。但基于 Sentinel 提供的各种规则对应的 loadRules API，我们可以自己实现规则的动态更新，而这一功能几乎在每个需要使用 Sentinel 的微服务项目中都需要实现一遍。Sentinel 也考虑到了这点，所以提供了动态数据源接口，并且提供了多种动态数据源的实现，尽管我们可能不会用到。</p>
<p>动态数据源作为扩展功能放在 sentinel-extension 模块下，前面我们学习的热点参数限流模块 sentinel-parameter-flow-control 也是在该模块下。在 1.7.1 版本，sentinel-extension 模块下的子模块除 sentinel-parameter-flow-control、sentinel-annotation-aspectj 之外，其余子模块都是实现动态数据源的模块。</p>
<ul>
<li>sentinel-datasource-extension：定义动态数据源接口、提供抽象类</li>
<li>sentinel-datasource-redis：基于 Redis 实现的动态数据源</li>
<li>sentinel-datasource-zookeeper： 基于 ZooKeeper 实现的动态数据源</li>
<li>其它省略</li>
</ul>
<p>显然，sentinel-datasource-extension 模块才是我们主要研究的模块，这是 Sentinel 实现动态数据源的核心。</p>
<h3>SentinelProperty</h3>
<p>SentinelProperty 是 Sentinel 提供的一个接口，可注册到 Sentinel 提供的各种规则的 Manager，例如 FlowRuleManager，并且可以给 SentinelProperty 添加监听器，在配置改变时，你可以调用 SentinelProperty#updateValue 方法，由它负责调用监听器去更新规则，而不需要调用 FlowRuleManager#loadRules 方法。同时，你也可以注册额外的监听器，在配置改变时做些别的事情。</p>
<p>SentinelProperty 并非 sentinel-datasource-extension 模块中定义的接口，而是 sentinel-core 定义的接口，其源码如下：</p>
<pre><code class="language-java">public interface SentinelProperty&lt;T&gt; {
    void addListener(PropertyListener&lt;T&gt; listener);
    void removeListener(PropertyListener&lt;T&gt; listener);
    boolean updateValue(T newValue);
}

</code></pre>
<ul>
<li>addListener：添加监听器</li>
<li>removeListener：移除监听器</li>
<li>updateValue：通知所有监听器配置更新，参数 newValue 为新的配置</li>
</ul>
<p>默认使用的实现类是 DynamicSentinelProperty，其实现源码如下（有删减）：</p>
<pre><code class="language-java">public class DynamicSentinelProperty&lt;T&gt; implements SentinelProperty&lt;T&gt; {
    // 存储注册的监听器
    protected Set&lt;PropertyListener&lt;T&gt;&gt; listeners = Collections.synchronizedSet(new HashSet&lt;PropertyListener&lt;T&gt;&gt;());
    @Override
    public void addListener(PropertyListener&lt;T&gt; listener) {
        listeners.add(listener);
        listener.configLoad(value);
    }
    @Override
    public void removeListener(PropertyListener&lt;T&gt; listener) {
        listeners.remove(listener);
    }
    @Override
    public boolean updateValue(T newValue) {
        for (PropertyListener&lt;T&gt; listener : listeners) {
            listener.configUpdate(newValue);
        }
        return true;
    }
}

</code></pre>
<p>可见，DynamicSentinelProperty 使用 Set 存储已注册的监听器，updateValue 负责通知所有监听器，调用监听器的 configUpdate 方法。</p>
<p>在前面分析 FlowRuleManager 时，我们只关注了其 loadRules 方法，除了使用 loadRules 方法加载规则配置之外，FlowRuleManager 还提供 registerProperty API，用于注册 SentinelProperty。</p>
<p>使用 SentinelProperty 实现加载 FlowRule 的步骤如下：</p>
<ol>
<li>给 FlowRuleManager 注册一个 SentinelProperty，替换 FlowRuleManager 默认创建的 SentinelProperty（因为默认的 SentinelProperty 外部拿不到）；</li>
<li>这一步由 FlowRuleManager 完成，FlowRuleManager 会给 SentinelProperty 注册 FlowPropertyListener 监听器，该监听器负责更新 FlowRuleManager.flowRules 缓存的限流规则；</li>
<li>在应用启动或者规则配置改变时，只需要调用 SentinelProperty#updateValue 方法，由 updateValue 通知 FlowPropertyListener 监听器去更新规则。</li>
</ol>
<p>FlowRuleManager 支持使用 SentinelProperty 加载或更新限流规则的实现源码如下：</p>
<pre><code class="language-java">public class FlowRuleManager {
    // 缓存限流规则
    private static final Map&lt;String, List&lt;FlowRule&gt;&gt; flowRules = new ConcurrentHashMap&lt;String, List&lt;FlowRule&gt;&gt;();
    // PropertyListener 监听器
    private static final FlowPropertyListener LISTENER = new FlowPropertyListener();
    // SentinelProperty
    private static SentinelProperty&lt;List&lt;FlowRule&gt;&gt; currentProperty 
       // 提供默认的 SentinelProperty
       = new DynamicSentinelProperty&lt;List&lt;FlowRule&gt;&gt;();

  static {
       // 给默认的 SentinelProperty 注册监听器（FlowPropertyListener）
        currentProperty.addListener(LISTENER);
  }

  // 注册 SentinelProperty
  public static void register2Property(SentinelProperty&lt;List&lt;FlowRule&gt;&gt; property) {
        synchronized (LISTENER) {
            currentProperty.removeListener(LISTENER);
            // 注册监听器
            property.addListener(LISTENER);
            currentProperty = property;
        }
  }
}

</code></pre>
<p>实现更新限流规则缓存的 FlowPropertyListener 是 FlowRuleManager 的一个内部类，其源码如下：</p>
<pre><code class="language-java">private static final class FlowPropertyListener implements PropertyListener&lt;List&lt;FlowRule&gt;&gt; {
        @Override
        public void configUpdate(List&lt;FlowRule&gt; value) {
            Map&lt;String, List&lt;FlowRule&gt;&gt; rules = FlowRuleUtil.buildFlowRuleMap(value);
            if (rules != null) {
                // 先清空缓存再写入
                flowRules.clear();
                flowRules.putAll(rules);
            }
        }
        @Override
        public void configLoad(List&lt;FlowRule&gt; conf) {
            Map&lt;String, List&lt;FlowRule&gt;&gt; rules = FlowRuleUtil.buildFlowRuleMap(conf);
            if (rules != null) {
                flowRules.clear();
                flowRules.putAll(rules);
            }
        }
}

</code></pre>
<p>PropertyListener 接口定义的两个方法：</p>
<ul>
<li>configUpdate：在规则更新时被调用，被调用的时机就是在 SentinelProperty#updateValue 方法被调用时。</li>
<li>configLoad：在规则首次加载时被调用，是否会被调用由 SentinelProperty 决定。DynamicSentinelProperty 就没有调用这个方法。</li>
</ul>
<p>所以，现在我们有两种方法更新限流规则：</p>
<ul>
<li>调用 FlowRuleManager#loadRules 方法</li>
<li>注册 SentinelProperty，调用 SentinelProperty#updateValue 方法</li>
</ul>
<h3>ReadableDataSource</h3>
<p>Sentinel 将读和写数据源抽离成两个接口，一开始只有读接口，写接口是后面才加的功能，目前来看，写接口只在热点参数限流模块中使用到。事实上，使用读接口就已经满足我们的需求。ReadableDataSource 接口的定义如下：</p>
<pre><code class="language-java">public interface ReadableDataSource&lt;S, T&gt; {
    T loadConfig() throws Exception;
    S readSource() throws Exception;
    SentinelProperty&lt;T&gt; getProperty();
    void close() throws Exception;
}

</code></pre>
<p>ReadableDataSource 是一个泛型接口，参数化类型 S 代表用于装载从数据源读取的配置的类型，参数化类型 T 代表对应 Sentinel 中的规则类型。例如，我们可以定义一个 FlowRuleProps 类，用于装载从 yml 配置文件中读取的限流规则配置，然后再将 FlowRuleProps 转为 FlowRule，所以 S 可以替换为 FlowRuleProps，T 可以替换为 <code>List&lt;FlowRule&gt;</code>。</p>
<p>ReadableDataSource 接口定义的方法解释说明如下：</p>
<ul>
<li>loadConfig：加载配置。</li>
<li>readSource：从数据源读取配置，数据源可以是 yaml 配置文件，可以是 MySQL、Redis 等，由实现类决定从哪种数据源读取配置。</li>
<li>getProperty：获取 SentinelProperty。</li>
<li>close：用于关闭数据源，例如使用文件存储配置时，可在此方法实现关闭文件输入流等。</li>
</ul>
<p>如果动态数据源提供 SentinelProperty，则可以调用 getProperty 方法获取动态数据源的 SentinelProperty，将 SentinelProperty 注册给规则管理器（XxxManager），动态数据源在读取到配置时就可以调用自身 SentinelProperty 的 updateValue 方法通知规则管理器（XxxManager）更新规则。</p>
<p>AbstractDataSource 是一个抽象类，该类实现 ReadableDataSource 接口，用于简化具体动态数据源的实现，子类只需要继承 AbstractDataSource 并实现 readSource 方法即可。AbstractDataSource 源码如下：</p>
<pre><code class="language-java">public abstract class AbstractDataSource&lt;S, T&gt; implements ReadableDataSource&lt;S, T&gt; {
    protected final Converter&lt;S, T&gt; parser;
    protected final SentinelProperty&lt;T&gt; property;

    public AbstractDataSource(Converter&lt;S, T&gt; parser) {
        if (parser == null) {
            throw new IllegalArgumentException(&quot;parser can't be null&quot;);
        }
        this.parser = parser;
        this.property = new DynamicSentinelProperty&lt;T&gt;();
    }

    @Override
    public T loadConfig() throws Exception {
        return loadConfig(readSource());
    }

    public T loadConfig(S conf) throws Exception {
        T value = parser.convert(conf);
        return value;
    }

    @Override
    public SentinelProperty&lt;T&gt; getProperty() {
        return property;
    }
}

</code></pre>
<p>从源码可以看出：</p>
<ul>
<li>AbstractDataSource 要求所有子类都必须提供一个数据转换器（Converter），Converter 用于将 S 类型的对象转为 T 类型对象，例如将 FlowRuleProps 对象转为 FlowRule 集合。</li>
<li>AbstractDataSource 在构造方法中创建 DynamicSentinelProperty，因此子类无需创建 SentinelProperty。</li>
<li>AbstractDataSource 实现 loadConfig 方法，首先调用子类实现的 readSource 方法从数据源读取配置，返回的对象类型为 S，再调用 Converter#convert 方法，将对象类型由 S 转为 T。</li>
</ul>
<p>Converter 接口的定义如下：</p>
<pre><code class="language-java">public interface Converter&lt;S, T&gt; {
    T convert(S source);
}

</code></pre>
<ul>
<li>convert：将类型为 S 的参数 source 转为类型为 T 的对象。</li>
</ul>
<h3>基于 Spring Cloud 动态配置实现规则动态配置</h3>
<p>我们项目中并未使用 Sentinel 提供的任何一种动态数据源的实现，而是选择自己实现数据源，因为我们项目是部署在 Kubernetes 集群上的，我们可以利用 ConfigMap 资源存储限流、熔断降级等规则。Spring Cloud Kubernetes 提供了 Spring Cloud 动态配置接口的实现，因此，我们不需要关心怎么去读取 ConfigMap 资源。就相当于基于 Spring Cloud 动态配置实现 Sentinel 规则动态数据源。Spring Cloud 动态配置如何使用这里不做介绍。</p>
<p>以实现 FlowRule 动态配置为例，其步骤如下。</p>
<p>第一步：定义一个用于装载动态配置的类，如 FlowRuleProps 所示。</p>
<pre><code class="language-java">@Component
@RefreshScope
@ConfigurationProperties(prefix = &quot;sentinel.flow-rules&quot;)
public class FlowRuleProps{
  //....省略
}

</code></pre>
<p>第二步：创建数据转换器，实现将 FlowRuleProps 转为 <code>List&lt;FlowRule&gt;</code>，如 FlowRuleConverter 所示。</p>
<pre><code class="language-java">public class FlowRuleConverter implements Converter&lt;FlowRuleProps, List&lt;FlowRule&gt;&gt;{

    @Override
    public List&lt;FlowRule&gt; convert(FlowRuleProps source){
       //....省略
    }
}

</code></pre>
<p>第三步：创建 FlowRuleDataSource，继承 AbstractDataSource，实现 readSource 方法。readSource 方法只需要获取 FlowRuleProps 返回即可，代码如下。</p>
<pre><code class="language-java">@Component
public class FlowRuleDataSource extends AbstractDataSource&lt;FlowRuleProps, List&lt;FlowRule&gt;&gt;{
    @Autowired
    private FlowRuleProps flowRuleProps;

    public FlowRuleDataSource() {
        super(new FlowRuleConverter());
    }
    @Override
    public FlowRuleProps readSource() throws Exception {
        return this.flowRuleProps;
    }
    @Override
    public void close() throws Exception {
    }
}

</code></pre>
<p>第四步：增强 FlowRuleDataSource，让 FlowRuleDataSource 能够监听到 FlowRuleProps 配置改变。</p>
<pre><code class="language-java">@Component
public class FlowRuleDataSource extends AbstractDataSource&lt;FlowRuleProps, List&lt;FlowRule&gt;&gt;
   implements ApplicationListener&lt;RefreshScopeRefreshedEvent&gt;,
        InitializingBean{
       // .....
    @Override
    public void onApplicationEvent(RefreshScopeRefreshedEvent event) {
        getProperty().updateValue(loadConfig());
    }

    @Override
    public void afterPropertiesSet() throws Exception {
        onApplicationEvent(new RefreshScopeRefreshedEvent());
    }
}

</code></pre>
<ul>
<li>实现 InitializingBean 方法，在数据源对象创建时，初始化加载一次规则配置。</li>
<li>实现 ApplicationListener 接口，监听动态配置改变事件（RefreshScopeRefreshedEvent），在监听到事件时，首先调用 loadConfig 方法加载所有限流规则配置，然后调用 getProperty 方法获取 SentinelProperty，最后调用 SentinelProperty#updateValue 方法通知 FlowRuleManager 的监听器更新限流规则缓存。</li>
</ul>
<p>第五步：写一个 ApplicationRunner 类，在 Spring 容器刷新完成后， 将数据源（FlowRuleDataSource）的 SentinelProperty 注册给 FlowRuleManager，代码如下。</p>
<pre><code class="language-java">@Component
public class FlowRuleDataSourceConfiguration implements ApplicationRunner{
    @Autowired
    private FlowRuleDataSource flowRuleDataSource;

    @Override
    public void run(ApplicationArguments args) throws Exception {
        // 将数据源的 SentinelProperty 注册给 FlowRuleManager
        FlowRuleManager.register2Property(flowRuleDataSource.getProperty());
    }
}

</code></pre>
<p>在调用 FlowRuleManager#register2Property 方法将 FlowRuleDataSource 动态数据源的 SentinelProperty 注册给 FlowRuleManager 时，FlowRuleManager 会自动给该 SentinelProperty 注册一个监听器（FlowPropertyListener）。</p>
<p>到此，一个基于 Spring Cloud 动态配置的限流规则动态数据源就已经完成，整个调用链路如下：</p>
<ol>
<li>当动态配置改变时，Spring Cloud 会发出 RefreshScopeRefreshedEvent 事件，FlowRuleDataSource 的 onApplicationEvent 方法被调用；</li>
<li>FlowRuleDataSource 调用 loadConfig 方法获取最新的配置；</li>
<li>FlowRuleDataSource#loadConfig 调用 readSource 方法获取 FlowRuleProps 对象，此时的 FlowRuleProps 对象已经装载了最新的配置；</li>
<li>FlowRuleDataSource#loadConfig 调用转换器（FlowRuleConverter）的 convert 方法将 FlowRuleProps 对象转为 <code>List&lt;FlowRule&gt;</code> 对象；</li>
<li>FlowRuleDataSource 调用自身的 SentinelProperty 的 updateValue 方法通知所有监听器，并携带新的规则配置；</li>
<li>FlowPropertyListener 监听器的 configUpdate 方法被调用；</li>
<li>FlowPropertyListener 在 configUpdate 方法中更新 FlowRuleManager 缓存的限流规则。</li>
</ol>
<h3>总结</h3>
<p>了解 Sentinel 实现动态数据源的原理后，我们可以灵活地自定义规则动态数据源，例如本篇介绍的，利用 Kubernetes 的 ConfigMap 资源存储规则配置，并通过 Spring Cloud 动态配置实现 Sentinel 的规则动态数据源。不仅如此，Sentinel 实现动态数据源的整体框架的设计也是值得我们学习的，如数据转换器、监听器。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="15&#32;自定义&#32;ProcessorSlot&#32;实现开关降级.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="17&#32;Sentinel&#32;主流框架适配.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4359828bef645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
