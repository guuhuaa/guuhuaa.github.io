<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>15 自定义 ProcessorSlot 实现开关降级.md</title>
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

                    <a class="current-tab" href="15&#32;自定义&#32;ProcessorSlot&#32;实现开关降级.md">15 自定义 ProcessorSlot 实现开关降级.md</a>
                    

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
                        <div><h1>15 自定义 ProcessorSlot 实现开关降级</h1>
<p>开关降级在我们公司的电商项目中是每个微服务都必须支持的一项功能，主要用于活动期间、每日流量高峰期间、主播带货期间关闭一些无关紧要功能，降低数据库的压力。</p>
<p>开关降级实现起来很简单，例如，我们可以使用 Spring AOP 或者动态代理模式拦截目标方法的执行，在方法执行之前，先根据 key 从 Redis 读取 value，如果 value 是 true，则不执行目标方法，直接响应服务降级。这种方式付出的性能损耗就只有一次 redis 的 get 操作，如果不想每个请求都读 Redis 缓存，也可以通过动态配置方式，使用配置中心去管理开关。</p>
<h3>使用 Spring AOP 实现开关降级功能</h3>
<p>以 Redis 缓存开关为例，使用切面实现开关降级只需要三步：定义注解、实现开关降级切面、在需要使用开关降级的接口方法上添加开关降级注解。</p>
<p>\1. 定义开关降级注解 @SwitchDegrade，代码如下：</p>
<pre><code class="language-java">@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.METHOD})
public @interface SwitchDegrade {
    // 缓存 key
    String key() default &quot;&quot;;
}

</code></pre>
<p>提示：如果是应用在实际项目中，建议为 @SwitchDegrade 注解添加一个前缀属性，限制同一个应用下的开关 key 都是有同一个前缀，避免多个应用之间的缓存 key 冲突。</p>
<p>\2. 实现切面 SwitchDegradeAspect，拦截接口方法的执行，代码如下：</p>
<pre><code class="language-java">@Aspect
public class SwitchDegradeAspect {
    // 切点定义
    @Pointcut(&quot;@annotation(com.wujiuye.demo.common.sentinel.SwitchDegrade)&quot;)
    public void degradePointCut() {
    }

    /**
     * 拦截请求判断是否开启开关降级
     */
    @Around(&quot;degradePointCut()&amp;&amp;@annotation(switchDegrade)&quot;)
    public Object around(ProceedingJoinPoint point, SwitchDegrade switchDegrade) throws Throwable {
        String cacheKey = switchDegrade.key();
        RedisTemplate redisTemplate = SpringContextUtils.getBean(RedisTemplate.class);
        String value = redisTemplate.get(cacheKey);
        if (&quot;true&quot;.equalsIgnoreCase(value)) {
            throw new SwitchDegradeException(cacheKey, &quot;开关降级打开&quot;);
        }
        return point.proceed();
    }
}

</code></pre>
<p>如代码所示，SwitchDegradeAspect 拦截目标方法的执行，先从方法上的 @SwitchDegrade 注解获取开关的缓存 key，根据 key 从 redis 读取当前开关的状态，如果 key 存在且 value 为 true，则抛出一个开关降级异常。</p>
<p>当开关打开时，SwitchDegradeAspect 并不直接响应请求，而是抛出异常由全局异常处理器处理，这是因为并不是每个接口方法都会有返回值，且返回值类型也不固定。所以还需要在全局异常处理器处理开关降级抛出的异常，代码如下：</p>
<pre><code class="language-java">    @ExceptionHandler(SwitchDegradeException.class)
    public BaseResponse handleSwitchDegradeException(SwitchDegradeException ex) {
        log.error(&quot;Switch Degrade! switch key is:{}, message:{}&quot;, ex.getSwitchKey(), ex.getMessage());
        return new BaseResponse(ResultCode.SERVICE_DEGRADE, ex.getMessage());
    }

</code></pre>
<p>提示：如果是整合 OpenFeign 使用，且配置了 Fallback，则全局异常可以不配置。</p>
<p>\3. 在需要被开关控制的接口方法上使用 @SwitchDegrade 注解，例如：</p>
<pre><code class="language-java">@RestController
@RequestMapping(&quot;/v1/test&quot;)
public class DemoController {
    @SwitchDegrade(key = &quot;auth:switch&quot;)
    @PostMapping(&quot;/demo&quot;)
    public GenericResponse&lt;Void&gt; demo(@RequestBody Invocation&lt;DemoFrom&gt; invocation) {
       //.....
    }
}

</code></pre>
<p>这种方式虽然能满足需求，但也有一个缺点，就是必须要在方法上添加 @SwitchDegrade 注解，配置不够灵活，但也不失为一个好方法。</p>
<h3>基于 Sentinel 自定义 ProcessorSlot 实现开关降级功能</h3>
<p>Sentinel 将降级功能的实现抽象为处理器插槽（ProcessorSlot），由一个个 ProcessorSlot 提供丰富的降级功能的实现，并且使用 SPI 机制提供扩展功能，使用者可通过自定义 SlotChainBuilder 自己构建 ProcessorSlotChain，这相当于给我们提供插件的功能。因此，我们可以通过自定义 ProcessorSlot 为 Sentinel 添加开关降级功能。</p>
<p>与熔断降级、限流降级一样，我们也先定义开关降级规则类，实现 loadRules API；然后提供一个 Checker，由 Checker 判断开关是否打开，是否需要拒绝当前请求；最后自定义 ProcessorSlot 与 SlotChainBuilder。</p>
<p>与使用切面实现开关降级有所不同，使用 Sentinel 实现开关降级我们不需要再在接口方法或者类上添加注解，我们想要实现的是与熔断降级、限流降级一样全部通过配置规则实现，这也是我们为什么选择基于 Sentinel 实现开关降级功能的原因。</p>
<p>通常，一个开关会控制很多的接口，而不仅仅只是一个，所以，一个开关对应一个降级规则，一个降级规则可配置多个资源。开关降级规则类 SwitchRule 实现代码如下：</p>
<pre><code class="language-java">@Data
@ToString
public class SwitchRule {
    public static final String SWITCH_KEY_OPEN = &quot;open&quot;;
    public static final String SWITCH_KEY_CLOSE = &quot;close&quot;;
    // 开关状态
    private String status = SWITCH_KEY_OPEN;
    // 开关控制的资源
    private Resources resources;
    @Data
    @ToString
    public static class Resources {
        // 包含
        private Set&lt;String&gt; include;
        // 排除
        private Set&lt;String&gt; exclude;
    }
}

</code></pre>
<p>灵活，不仅仅只是去掉注解的使用，更需要可以灵活指定开关控制某些资源，因此，配置开关控制的资源应支持这几种情况：指定该开关只控制哪些资源、除了某些资源外其它都受控制、控制全部。所以，SwitchRule 的资源配置与 Sentinel 的熔断降级、限流降级规则配置不一样，SwitchRule 支持三种资源配置方式：</p>
<ul>
<li>如果资源不配置，则开关作用到全部资源；</li>
<li>如果配置 inclode，则作用到 include 指定的所有资源；</li>
<li>如果不配置 inclode 且配置了 exclude，则除了 exclude 指定的资源外，其它资源都受这个开关的控制。</li>
</ul>
<p>接着实现 loadRules API。在 Sentinel 中，提供 loadRules API 的类通常命名为 XxxRuleManager，即 Xxx 规则管理器，所以我们定义的开关降级规则管理器命名为 SwitchRuleManager。SwitchRuleManager 的实现代码如下：</p>
<pre><code class="language-java">public class SwitchRuleManager {
    private static volatile Set&lt;SwitchRule&gt; switchRuleSet = new HashSet&lt;&gt;();
    public static void loadSwitchRules(Set&lt;SwitchRule&gt; rules) {
        SwitchRuleManager.switchRuleSet = rules;
    }
    static Set&lt;SwitchRule&gt; getRules() {
        return switchRuleSet;
    }
}

</code></pre>
<p>SwitchRuleManager 提供两个接口：</p>
<ul>
<li>loadSwitchRules：用于更新或者加载开关降级规则</li>
<li>getRules：获取当前生效的全部开关降级规则</li>
</ul>
<p>同样地，在 Sentinel 中，一般会将检查规则是否达到触发降级的阈值由 XxxRuleChecker 完成，即 Xxx 规则检查员，所以我们定义的开关降级规则检查员命名为 SwitchRuleChecker，由 SwitchRuleChecker 检查开关是否打开，如果开关打开则触发开关降级。SwitchRuleChecker 的代码实现如下：</p>
<pre><code class="language-java">public class SwitchRuleChecker {

    public static void checkSwitch(ResourceWrapper resource, Context context) throws SwitchException {
        Set&lt;SwitchRule&gt; switchRuleSet = SwitchRuleManager.getRules();
        // 遍历规则
        for (SwitchRule rule : switchRuleSet) {
            // 判断开关状态，开关未打开则跳过
            if (!rule.getStatus().equalsIgnoreCase(SwitchRule.SWITCH_KEY_OPEN)) {
                continue;
            }
            if (rule.getResources() == null) {
                continue;
            }
            // 实现 include 语意
            if (!CollectionUtils.isEmpty(rule.getResources().getInclude())) {
                if (rule.getResources().getInclude().contains(resource.getName())) {
                    throw new SwitchException(resource.getName(), &quot;switch&quot;);
                }
            }
            // 实现 exclude 语意
            if (!CollectionUtils.isEmpty(rule.getResources().getExclude())) {
                if (!rule.getResources().getExclude().contains(resource.getName())) {
                    throw new SwitchException(resource.getName(), &quot;switch&quot;);
                }
            }
        }
    }

}

</code></pre>
<p>如代码所示，SwitchRuleChecker 从 SwitchRuleManager 获取配置的开关降级规则，遍历开关降级规则，如果开关打开，且匹配到当前资源名称被该开关控制，则抛出 SwitchException。</p>
<p>SwitchException 需继承 BlockException，抛出的 SwitchException 如果不被捕获，则由全局异常处理器处理。一定是要抛出 BlockException 的子类，否则抛出的异常会被资源指标数据统计收集，会影响到熔断降级等功能的准确性。</p>
<p>虽然 SwitchRuleChecker 使用了 for 循环遍历开关降级规则，但一个项目中的开关是很少的，一般就一个或者几个。</p>
<p>与熔断降级、限流降级一样，开关降级也支持一个资源被多个开关规则控制。</p>
<p>最后，还需要自定义实现开关降级功能的切入点 SwitchSlot。SwitchSlot 继承 AbstractLinkedProcessorSlot，在 entry 方法中调用 SwitchRuleChecker#checkSwitch 方法检查当前资源是否已经降级。SwitchSlot 的代码实现如下：</p>
<pre><code class="language-java">public class SwitchSlot extends AbstractLinkedProcessorSlot&lt;Object&gt; {

    @Override
    public void entry(Context context, ResourceWrapper resourceWrapper, Object param, int count, boolean prioritized, Object... args) throws Throwable {
        SwitchRuleChecker.checkSwitch(resourceWrapper, context);
        fireEntry(context, resourceWrapper, param, count, prioritized, args);
    }

    @Override
    public void exit(Context context, ResourceWrapper resourceWrapper, int count, Object... args) {
        fireExit(context, resourceWrapper, count, args);
    }

}

</code></pre>
<p>自定义 ProcessorSlotChain 构建器 MySlotChainBuilder，将自定义的 SwitchSlot 添加到 ProcessorSlot 链表的末尾。当然，可以添加到任何位置，因为 SwitchSlot 没有用到指标数据，SwitchSlot 放置何处都不会影响到 Sentinel 的正常工作。</p>
<p>MySlotChainBuilder 代码实现如下：</p>
<pre><code class="language-java">public class MySlotChainBuilder extends DefaultSlotChainBuilder {
    @Override
    public ProcessorSlotChain build() {
        ProcessorSlotChain chain = super.build();
        chain.addLast(new SwitchSlot());
        return chain;
    }
}

</code></pre>
<p>MySlotChainBuilder 继承 DefaultSlotChainBuilder 只是为了使用 DefaultSlotChainBuilder#build 方法，简化 ProcessorSlotChain 的构造步骤，只需要在 DefaultSlotChainBuilder 构造的链表尾部添加一个 SwitchSlot 即可。</p>
<p>现在 MySlotChainBuilder 生效了吗？当然还不行，还需要将 MySlotChainBuilder 注册到 SlotChainBuilder 接口的配置文件。</p>
<p>在当前项目的 resources 资源目录的 META-INF/service 目录下创建一个名为“com.alibaba.csp.sentinel.slotchain.SlotChainBuilder”的文件，在该文件中配置 MySlotChainBuilder 类的全名，例如：</p>
<pre><code class="language-txt">com.wujiuye.demo.common.sentinel.MySlotChainBuilder

</code></pre>
<p>现在，您可以在 MySlotChainBuilder#build 方法中添加断点，然后启动项目，正常情况下程序会在该断点停下。但由于我们并未配置开关降级规则，所以还看不到效果。</p>
<p>我们可以写一个配置类，在配置类调用 SwitchRuleManager#loadRules API 添加开关降级规则。例如：</p>
<pre><code class="language-java">@Configuration
public class SentinelRuleConfiguration{

    static {
           Set&lt;SwitchRule&gt; rules = new HashSet&lt;&gt;();
            // 
            SwitchRule rule = new SwitchRule();
            rule.setStatus(SwitchRule.SWITCH_KEY_OPEN);
            SwitchRule.Resources resources = new SwitchRule.Resources();
            Set&lt;String&gt; include = new HashSet&lt;&gt;();
            include.add(&quot;/v1/test/demo&quot;);
            resources.setInclude(include);
            // 
            rules.add(rule);
            SwitchRuleManager.loadSwitchRules(rules);
    }
}

</code></pre>
<p>上面代码配置了一个开关降级规则，该降级规则只控制接口（资源）<code>&quot;/v1/test/demo&quot;</code>，SwitchRule.status 控制开关是否打开，测试这里就不演示了。当然，这种配置方式只适用于本地测试，实际项目中我们可通过动态配置实现，这将在后面介绍 Sentinel 动态数据源时再介绍如何实现。</p>
<p>提示：实现动态配置规则并不一定需要使用 Sentinel 的动态数据源。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="14&#32;黑白名单限流与热点参数限流.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="16&#32;Sentinel&#32;动态数据源：规则动态配置.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43597dad79645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
