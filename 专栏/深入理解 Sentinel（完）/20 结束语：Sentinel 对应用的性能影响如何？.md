<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>20 结束语：Sentinel 对应用的性能影响如何？.md</title>
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

                    <a class="current-tab" href="20&#32;结束语：Sentinel&#32;对应用的性能影响如何？.md">20 结束语：Sentinel 对应用的性能影响如何？.md</a>
                    

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
                        <div><h1>20 结束语：Sentinel 对应用的性能影响如何？</h1>
<p>“引入 Sentinel 带来的性能损耗非常小，只有在业务单机量级超过 25W QPS 的时候才会有一些显著的影响（5%~10% 左右），单机 QPS 不太大的时候损耗几乎可以忽略不计。”</p>
<p>这是官方文档写的一段话，那么性能到底如何呢？本篇我们回顾 Sentinel 的源码，看看 Sentinel 在性能方面所做出的努力，最后使用 JMH 做个简单的基准测试，看看 Sentinel 表现如何，在此之前也会详细介绍 JMH 的使用。</p>
<h3>Sentinel 在性能方面做出了哪些努力？</h3>
<h4><strong>滑动窗口指标数据统计</strong></h4>
<p>Sentinel 统计指标数据使用的是滑动窗口：时间窗口+Bucket，通过循环复用 Bucket 以减少 Bucket 的创建和销毁。在统计指标数据时，利用当前时间戳定位 Bucket，使用 LongAdder 统计时间窗口内的请求成功数、失败数、总耗时等指标数据优化了并发锁。Sentinel 通过定时任务递增时间戳以获取当前时间戳，避免了每次获取时间戳都使用 System 获取的性能消耗。</p>
<h4><strong>使用 Map 而不使用 ConcurrentMap</strong></h4>
<p>Sentinel 中随处可见的加锁重新创建 Map，例如：</p>
<pre><code class="language-java">        ProcessorSlotChain chain = chainMap.get(resourceWrapper);
        if (chain == null) {
            synchronized (LOCK) {
                chain = chainMap.get(resourceWrapper);
                if (chain == null) {
                    chain = SlotChainProvider.newSlotChain();
                    // 创建新的 map
                    Map&lt;ResourceWrapper, ProcessorSlotChain&gt; newMap = new HashMap&lt;ResourceWrapper, ProcessorSlotChain&gt;(
                        chainMap.size() + 1);
                    // 插入当前 map 存储的数据
                    newMap.putAll(chainMap);
                    // 插入新创建的 key-value
                    newMap.put(resourceWrapper, chain);
                    // 替换旧的
                    chainMap = newMap;
                }
            }
        }
        return chain;

</code></pre>
<p>Sentinel 使用 Map 而非 ConcurrentMap 是为了尽量避免加锁，大多数场景都是读多写少，以上面代码为例，ProcessorSlotChain 的新增只在资源第一次被访问时，例如接口第一次被调用，而后续都不会再写。假设有 10 个接口，这 10 个接口在应用启动起来就都被访问过了，那么这个 Map 后续就不会再出现写的情况，既然不会再有写操作，就没有必须加锁了，所以使用 Map 而不是使用 ConcurrentMap。</p>
<h4><strong>流量效果控制</strong></h4>
<p>RateLimiterController 匀速限流控制器的实现只支持最大 1000QPS，这是因为 Sentinel 获取的当前时间戳是通过定时任务累加的，每毫秒一次，所以 Sentinel 在实现匀速限流或冷启动限流使用的时间戳最小单位都是毫秒。以毫秒为最小单位，那么 1 秒钟最大能通过的请求数当然也就只有 1000，这是出于性能方面的考虑。</p>
<p>可能很多人在使用 Sentinel 的过程中都发现了，RateLimiterController 实现的匀速并不那么严格，例如想要限制每 5 毫秒通过一个请求，但实际上可能每 5 毫秒通过好几个请求，这与 CPU 核心线程数有关，因为 Sentinel 并不严格控制并发下的排队计时，这也是出于性能的考虑。实现项目中，我们也并不对匀速要求那么严格，所以这些缺点是可以接受的。</p>
<p>WarmUpController 冷启动限流效果的实现并不控制每个请求的通过时间间隔，只是每秒钟生产一次令牌，并且在生产令牌后扣减与上一秒通过的请求数相等数量的令牌，Sentinel 的作者称这个行为叫令牌自动掉落，这些也都是出于性能方面的考虑。</p>
<p>仅从以上这些细节我们也能看到 Sentinel 在性能方面所做出的努力，Sentinel 尽最大可能降低自身对应用的影响，这些是值得称赞的地方。</p>
<h3>基准测试工具 JMH</h3>
<p>基准测试 Benchmark 是测量、评估软件性能指标的一种测试，对某个特定目标场景的某项性能指标进行定量的和可对比的测试。JMH 即 Java Microbenchmark Harness，是 Java 用来做基准测试的一个工具，该工具由 OpenJDK 提供并维护，测试结果可信度高。</p>
<p>我们可以将 JMH 直接用在需要进行基准测试的项目中，以单元测试方式使用，需要在项目中引入 JMH 的 jar 包，依赖配置如下。</p>
<pre><code class="language-xml">&lt;dependencies&gt;
    &lt;dependency&gt;
        &lt;groupId&gt;org.openjdk.jmh&lt;/groupId&gt;
        &lt;artifactId&gt;jmh-core&lt;/artifactId&gt;
        &lt;version&gt;1.23&lt;/version&gt;
    &lt;/dependency&gt;
    &lt;dependency&gt;
        &lt;groupId&gt;org.openjdk.jmh&lt;/groupId&gt;
        &lt;artifactId&gt;jmh-generator-annprocess&lt;/artifactId&gt;
        &lt;version&gt;1.23&lt;/version&gt;
    &lt;/dependency&gt;
&lt;/dependencies&gt;

</code></pre>
<p>注：1.23 版本是 JMH 目前最新的版本。</p>
<h4><strong>注解方式使用</strong></h4>
<p>在运行时，注解配置被用于解析生成 BenchmarkListEntry 配置类实例。一个方法对应一个 @Benchmark 注解，一个 @Benchmark 注解对应一个基准测试方法。注释在类上的注解，或者注释在类的字段上的注解，则是类中所有基准测试方法共用的配置。</p>
<p><strong>@Benchmark</strong></p>
<p>@Benchmark 注解用于声明一个 public 方法为基准测试方法，如下代码所示。</p>
<pre><code class="language-java">public class MyTestBenchmark {

    @Benchmark
    @Test
    public void testFunction() {
        // 
    }

}

</code></pre>
<p><strong>@BenchmarkMode</strong></p>
<p>通过 JMH 我们可以轻松的测试出某个接口的吞吐量、平均执行时间等指标的数据。假设我们想测试某个方法的平均耗时，那么可以使用 @BenchmarkMode 注解指定测试维度为 Mode.AverageTime，代码如下。</p>
<pre><code class="language-java">public class MyTestBenchmark {

    @BenchmarkMode(Mode.AverageTime) 
    @Benchmark
    @Test
    public void testFunction() {
        //
    }

}

</code></pre>
<p><strong>@Measurement</strong></p>
<p>假设我们需要测量五次，那么可以使用 @Measurement 注解，代码如下。</p>
<pre><code class="language-java">public class MyTestBenchmark {

    @Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
    @BenchmarkMode(Mode.AverageTime)
    @Benchmark
    @Test
    public void testFunction() {
        //
    }

}

</code></pre>
<p>@Measurement 注解有三个配置项：</p>
<ul>
<li>iterations：测量次数。</li>
<li>time 与 timeUnit：测量一次的持续时间，timeUnit 指定时间单位，本例中每次测量持续 1 秒，1 秒内执行的 testFunction 方法的次数是不固定的，由方法执行耗时和 time 决定。</li>
</ul>
<p><strong>@Warmup</strong></p>
<p>为了数据准确，我们可能需要让被测试的方法做下热身运动，一定的预热次数可提升测试结果的准备度。可使用 @Warmup 注解声明需要预热的次数、每次预热的持续时间，代码如下。</p>
<pre><code class="language-java">public class MyTestBenchmark {

    @Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
    @Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
    @BenchmarkMode(Mode.AverageTime)
    @Benchmark
    @Test
    public void testFunction() {
       //
    }

}

</code></pre>
<p>@Warmup 注解有三个配置项：</p>
<ul>
<li>iterations：预热次数。</li>
<li>time 与 timeUnit：预热一次的持续时间，timeUnit 指定时间单位。</li>
</ul>
<p>假设 @Measurement 指定 iterations 为 100，time 为 10s，则：每个线程实际执行基准测试方法的次数等于 time 除以基准测试方法单次执行的耗时，假设基准测试方法执行耗时为 1s，那么一次测量最多只执行 10（time 为 10s / 方法执行耗时 1s）次基准测试方法，而 iterations 为 100 指的是测试 100 次（不是执行 100 次基准测试方法）。</p>
<p><strong>@OutputTimeUnit</strong></p>
<p>@OutputTimeUnit 注解用于指定输出的方法执行耗时的单位。</p>
<p>如果方法执行耗时为毫秒级别，为了便于观察结果，我们可以使用 @OutputTimeUnit 指定输出的耗时时间单位为毫秒，否则使用默认的秒做单位，会输出 10 的负几次方这样的数字，不太直观。</p>
<pre><code class="language-java">public class MyTestBenchmark {

    @OutputTimeUnit(TimeUnit.NANOSECONDS)
    @Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
    @Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
    @BenchmarkMode(Mode.AverageTime)
    @Benchmark
    @Test
    public void testFunction() {
        // 
    }

}

</code></pre>
<p><strong>@Fork</strong></p>
<p>@Fork 注解用于指定 fork 出多少个子进程来执行同一基准测试方法。</p>
<p>假设我们不需要多个进程，那么可以使用 @Fork 指定进程数为 1，如下代码所示。</p>
<pre><code class="language-java">public class MyTestBenchmark {

    @Fork(1)
    @OutputTimeUnit(TimeUnit.NANOSECONDS)
    @Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
    @Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
    @BenchmarkMode(Mode.AverageTime)
    @Benchmark
    @Test
    public void testFunction() {
        //
    }

}

</code></pre>
<p><strong>@Threads</strong></p>
<p>@Threads 注解用于指定使用多少个线程来执行基准测试方法，如果使用 @Threads 指定线程数为 2，那么每次测量都会创建两个线程来执行基准测试方法。</p>
<pre><code class="language-java">public class MyTestBenchmark {

    @Threads(2)
    @Fork(1)
    @OutputTimeUnit(TimeUnit.NANOSECONDS)
    @Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
    @BenchmarkMode(Mode.AverageTime)
    @Benchmark
    @Test
    public void testFunction() {
        // 
    }

}

</code></pre>
<p>如果 @Measurement 注解指定 time 为 1s，基准测试方法的执行耗时为 1s，那么如果只使用单个线程，一次测量只会执行一次基准测试方法，如果使用 10 个线程，一次测量就能执行 10 次基准测试方法。</p>
<p><strong>公共注解</strong></p>
<p>假设我们需要在 MyTestBenchmark 类中创建两个基准测试方法，一个是 testFunction1，另一个是 testFunction2，这两个方法分别调用不同的支付接口，用于对比两个接口的性能。那么我们可以将除 @Benchmark 注解外的其它注解都声明到类上，让两个基准测试方法都使用同样的配置，代码如下。</p>
<pre><code class="language-java">@BenchmarkMode(Mode.AverageTime)
@Fork(1)
@Threads(2)
@OutputTimeUnit(TimeUnit.NANOSECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
public class MyTestBenchmark {

    @Benchmark
    @Test
    public void testFunction1() {
        // 
    }

    @Benchmark
    @Test
    public void testFunction2() {
        // 
    }
}

</code></pre>
<p>下面我们以测试 Gson、Jackson 两个 JSON 解析框架的性能对比为例。</p>
<pre><code class="language-java">@BenchmarkMode(Mode.AverageTime)
@Fork(1)
@Threads(2)
@OutputTimeUnit(TimeUnit.NANOSECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@State(Scope.Benchmark)
public class JsonBenchmark {

     private GsonParser gsonParser = new GsonParser();
     private JacksonParser jacksonParser = new JacksonParser();

    @Benchmark
    @Test
    public void testGson() {
        gsonParser.fromJson(&quot;{\&quot;startDate\&quot;:\&quot;2020-04-01 16:00:00\&quot;,\&quot;endDate\&quot;:\&quot;2020-05-20 13:00:00\&quot;,\&quot;flag\&quot;:true,\&quot;threads\&quot;:5,\&quot;shardingIndex\&quot;:0}&quot;, JsonTestModel.class);
    }

    @Benchmark
    @Test
    public void testJackson() {
        jacksonParser.fromJson(&quot;{\&quot;startDate\&quot;:\&quot;2020-04-01 16:00:00\&quot;,\&quot;endDate\&quot;:\&quot;2020-05-20 13:00:00\&quot;,\&quot;flag\&quot;:true,\&quot;threads\&quot;:5,\&quot;shardingIndex\&quot;:0}&quot;, JsonTestModel.class);
    }
}

</code></pre>
<p>我们可以使用 @State 注解指定 gsonParser、jacksonParser 这两个字段的共享域。</p>
<p>在本例中，我们使用 @Threads 注解声明创建两个线程来执行基准测试方法，假设我们配置 @State(Scope.Thread)，那么在不同线程中，gsonParser、jacksonParser 这两个字段都是不同的实例。</p>
<p>以 testGson 方法为例，我们可以认为 JMH 会为每个线程克隆出一个 gsonParser 对象。如果在 testGson 方法中打印 gsonParser 对象的 hashCode，你会发现，相同线程打印的结果相同，不同线程打印的结果不同。例如：</p>
<pre><code class="language-java">@BenchmarkMode(Mode.AverageTime)
@Fork(1)
@Threads(2)
@OutputTimeUnit(TimeUnit.NANOSECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@State(Scope.Thread)
public class JsonBenchmark {

     private GsonParser gsonParser = new GsonParser();
     private JacksonParser jacksonParser = new JacksonParser();

    @Benchmark
    @Test
    public void testGson() {
        System.out.println(&quot;current Thread:&quot; + Thread.currentThread().getName() + &quot;==&gt;&quot; + gsonParser.hashCode());
        gsonParser.fromJson(&quot;{\&quot;startDate\&quot;:\&quot;2020-04-01 16:00:00\&quot;,\&quot;endDate\&quot;:\&quot;2020-05-20 13:00:00\&quot;,\&quot;flag\&quot;:true,\&quot;threads\&quot;:5,\&quot;shardingIndex\&quot;:0}&quot;, JsonTestModel.class);
    }

    @Benchmark
    @Test
    public void testJackson() {
        jacksonParser.fromJson(&quot;{\&quot;startDate\&quot;:\&quot;2020-04-01 16:00:00\&quot;,\&quot;endDate\&quot;:\&quot;2020-05-20 13:00:00\&quot;,\&quot;flag\&quot;:true,\&quot;threads\&quot;:5,\&quot;shardingIndex\&quot;:0}&quot;, JsonTestModel.class);
    }
}

</code></pre>
<p>执行 testGson 方法输出的结果如下：</p>
<pre><code class="language-text">current Thread:com.msyc.common.JsonBenchmark.testGson-jmh-worker-1==&gt;2063684770
current Thread:com.msyc.common.JsonBenchmark.testGson-jmh-worker-2==&gt;1629232880
current Thread:com.msyc.common.JsonBenchmark.testGson-jmh-worker-1==&gt;2063684770
current Thread:com.msyc.common.JsonBenchmark.testGson-jmh-worker-2==&gt;1629232880
current Thread:com.msyc.common.JsonBenchmark.testGson-jmh-worker-1==&gt;2063684770
current Thread:com.msyc.common.JsonBenchmark.testGson-jmh-worker-2==&gt;1629232880
current Thread:com.msyc.common.JsonBenchmark.testGson-jmh-worker-1==&gt;2063684770
current Thread:com.msyc.common.JsonBenchmark.testGson-jmh-worker-2==&gt;1629232880
......

</code></pre>
<p><strong>@Param</strong></p>
<p>使用 @Param 注解可指定基准方法执行参数，@Param 注解只能指定 String 类型的值，可以是一个数组，参数值将在运行期间按给定顺序遍历。假设 @Param 注解指定了多个参数值，那么 JMH 会为每个参数值执行一次基准测试。</p>
<p>例如，我们想测试不同复杂度的 JSON 字符串使用 Gson 框架与使用 Jackson 框架解析的性能对比，代码如下。</p>
<pre><code class="language-java">@BenchmarkMode(Mode.AverageTime)
@Fork(1)
@Threads(2)
@OutputTimeUnit(TimeUnit.NANOSECONDS)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@State(Scope.Thread)
public class JsonBenchmark {

    private GsonParser gsonParser = new GsonParser();
    private JacksonParser jacksonParser = new JacksonParser();

    // 指定参数有三个值
    @Param(value = 
                {&quot;{\&quot;startDate\&quot;:\&quot;2020-04-01 16:00:00\&quot;,\&quot;endDate\&quot;:\&quot;2020-05-20 13:00:00\&quot;,\&quot;flag\&quot;:true,\&quot;threads\&quot;:5,\&quot;shardingIndex\&quot;:0}&quot;,
                &quot;{\&quot;startDate\&quot;:\&quot;2020-04-01 16:00:00\&quot;,\&quot;endDate\&quot;:\&quot;2020-05-20 14:00:00\&quot;}&quot;,
                &quot;{\&quot;flag\&quot;:true,\&quot;threads\&quot;:5,\&quot;shardingIndex\&quot;:0}&quot;})
    private String jsonStr;

    @Benchmark
    @Test
    public void testGson() {
        gsonParser.fromJson(jsonStr, JsonTestModel.class);
    }

    @Benchmark
    @Test
    public void testJackson() {
        jacksonParser.fromJson(jsonStr, JsonTestModel.class);
    }

}

</code></pre>
<p>测试结果如下：</p>
<pre><code class="language-text">Benchmark                                                                                                                      (jsonStr)  Mode  Cnt      Score       Error  Units
JsonBenchmark.testGson     {&quot;startDate&quot;:&quot;2020-04-01 16:00:00&quot;,&quot;endDate&quot;:&quot;2020-05-20 13:00:00&quot;,&quot;flag&quot;:true,&quot;threads&quot;:5,&quot;shardingIndex&quot;:0}  avgt    5  12180.763 ±  2481.973  ns/op

JsonBenchmark.testGson                                               {&quot;startDate&quot;:&quot;2020-04-01 16:00:00&quot;,&quot;endDate&quot;:&quot;2020-05-20 14:00:00&quot;}  avgt    5   8154.709 ±  3393.881  ns/op

JsonBenchmark.testGson                                                                       {&quot;flag&quot;:true,&quot;threads&quot;:5,&quot;shardingIndex&quot;:0}  avgt    5   9994.171 ±  5737.958  ns/op

JsonBenchmark.testJackson  {&quot;startDate&quot;:&quot;2020-04-01 16:00:00&quot;,&quot;endDate&quot;:&quot;2020-05-20 13:00:00&quot;,&quot;flag&quot;:true,&quot;threads&quot;:5,&quot;shardingIndex&quot;:0}  avgt    5  15663.060 ±  9042.672  ns/op

JsonBenchmark.testJackson  {&quot;startDate&quot;:&quot;2020-04-01 16:00:00&quot;,&quot;endDate&quot;:&quot;2020-05-20 14:00:00&quot;}  avgt    5  13776.828 ± 11006.412  ns/op

JsonBenchmark.testJackson                                                            {&quot;flag&quot;:true,&quot;threads&quot;:5,&quot;shardingIndex&quot;:0}  avgt    5   9824.283 ±   311.555  ns/op

</code></pre>
<h4><strong>非注解方式使用</strong></h4>
<p>通过使用 OptionsBuilder 构造一个 Options，并创建一个 Runner，调用 Runner 的 run 方法就能执行基准测试。</p>
<p>使用非注解方式实现上面的例子，代码如下。</p>
<pre><code class="language-java">public class BenchmarkTest{

    @Test
    public void test() throws RunnerException {
        Options options = new OptionsBuilder()
                .include(JsonBenchmark.class.getSimpleName())
                .exclude(&quot;testJackson&quot;)
                .forks(1)
                .threads(2)
                .timeUnit(TimeUnit.NANOSECONDS)
                .warmupIterations(5)
                .warmupTime(TimeValue.seconds(1))
                .measurementIterations(5)
                .measurementTime(TimeValue.seconds(1))
                .mode(Mode.AverageTime)
                .build();
        new Runner(options).run();
    }

}

</code></pre>
<ul>
<li>include：导入一个基准测试类。调用方法传递的是类的简单名称，不含包名。</li>
<li>exclude：排除哪些方法。默认 JMH 会为 include 导入的类的每个 public 方法都当成是基准测试方法，这时我们就可以使用 exclude 排除不需要参与基准测试的方法。如本例中使用 exclude 排除了 testJackson 方法。</li>
</ul>
<p>使用注解与不使用注解其实都是一样，只不过使用注解更加方便。在运行时，注解配置被用于解析生成 BenchmarkListEntry 配置类实例，而在代码中使用 Options 配置也是被解析成一个个 BenchmarkListEntry 配置类实例（每个方法对应一个）。</p>
<h4><strong>打 jar 包放服务器上执行</strong></h4>
<p>对于 JSON 解析框架性能对比我们可以使用单元测试，而如果想要测试 Web 服务的某个接口性能，需要对接口进行压测，就不能使用简单的单元测试方式去测，我们可以独立创建一个接口测试项目，将基准测试代码写在该项目中，然后将写好的基准测试项目打包成 jar 包丢到 Linux 服务器上执行，测试结果会更准确一些，硬件、系统贴近线上环境、也不受本机开启的应用数、硬件配置等因素影响。</p>
<p>使用 Java 命令即可运行一个基准测试应用：</p>
<pre><code class="language-shell">java -jar my-benchmarks.jar

</code></pre>
<h4>在 IDEA 中执行</h4>
<p>在 IDEA 中，我们可以编写一个单元测试方法，在单元测试方法中创建一个 org.openjdk.jmh.runner.Runner，调用 Runner 的 run 方法执行基准测试。但 JMH 不会去扫描包，不会执行每个基准测试方法，这需要我们通过配置项来告知 JMH 需要执行哪些基准测试方法。</p>
<pre><code class="language-java">public class BenchmarkTest{

    @Test
    public void test() throws RunnerException {
        Options options = null; // 创建 Options
        new Runner(options).run();
    }

}

</code></pre>
<p>完整例子如下：</p>
<pre><code class="language-java">public class BenchmarkTest{
     @Test
     public void test() throws RunnerException {
        Options options = new OptionsBuilder()
                 .include(JsonBenchmark.class.getSimpleName())
                 // .output(&quot;/tmp/json_benchmark.log&quot;)
                 .build();
        new Runner(options).run();
     }
}

</code></pre>
<p>Options 在前面已经介绍过了，由于本例中 JsonBenchmark 这个类已经使用了注解，因此 Options 只需要配置需要执行基准测试的类。如果需要执行多个基准测试类，include 方法可以多次调用。如果需要将测试结果输出到文件，可调用 output 方法配置文件路径，不配置则输出到控制台。</p>
<h4><strong>在 IDEA 中使用插件 JMH Plugin 执行</strong></h4>
<p>插件源码地址：</p>
<blockquote>
<p><a href="https://github.com/artyushov/idea-jmh-plugin">https://github.com/artyushov/idea-jmh-plugin</a></p>
</blockquote>
<p>安装：在 IDEA 中搜索 JMH Plugin，安装后重启即可使用。</p>
<p><strong>1. 只执行单个 Benchmark 方法</strong></p>
<p>在方法名称所在行，IDEA 会有一个▶️执行符号，右键点击运行即可。如果写的是单元测试方法，IDEA 会提示你选择执行单元测试还是基准测试。</p>
<p><strong>2. 执行一个类中的所有 Benchmark 方法</strong></p>
<p>在类名所在行，IDEA 会有一个<code>▶️</code>执行符号，右键点击运行，该类下的所有被 @Benchmark 注解注释的方法都会执行。如果写的是单元测试方法，IDEA 会提示你选择执行单元测试还是基准测试。</p>
<h3>使用 JMH 对 Sentinel 做压测</h3>
<p>要测试 Sentinel 对应用性能的影响，我们需要测试两组数据进行对比，分别是不使用 Sentinel 的情况下方法的吞吐量、使用 Sentinel 保护方法后方法的吞吐量。</p>
<p>下面是 Sentinel 提供的基准测试类部分源码。</p>
<pre><code class="language-java">@Fork(1)
@Warmup(iterations = 10)
@BenchmarkMode(Mode.Throughput)
@OutputTimeUnit(TimeUnit.SECONDS)
@State(Scope.Thread)
public class SentinelEntryBenchmark {

    @Param({&quot;25&quot;, &quot;50&quot;, &quot;100&quot;, &quot;200&quot;, &quot;500&quot;, &quot;1000&quot;})
    private int length;
    private List&lt;Integer&gt; numbers;

    @Setup
    public void prepare() {
        numbers = new ArrayList&lt;&gt;();
        for (int i = 0; i &lt; length; i++) {
            numbers.add(ThreadLocalRandom.current().nextInt());
        }
    }

    @Benchmark
    @Threads(8)
    public void doSomething() {
        Collections.shuffle(numbers);
        Collections.sort(numbers);
    }

    @Benchmark
    @Threads(8)
    public void doSomethingWithEntry() {
        Entry e0 = null;
        try {
            e0 = SphU.entry(&quot;benchmark&quot;);
            doSomething();
        } catch (BlockException e) {
        } finally {
            if (e0 != null) {
                e0.exit();
            }
        }
    }

}

</code></pre>
<p>该基准测试类使用 @State 指定每个线程使用不同的 numbers 字段的实例，所以 @Setup 注解的方法也会执行 8 次，分别是在每个线程开始执行基准测试方法之前执行，用于完成初始化工作，与 Junit 中的 @Before 注解功能相似。</p>
<p>doSomething 方法用于模拟业务方法，doSomethingWithEntry 方法用于模拟使用 Sentinel 保护业务方法，分别对这两个方法进行基准测试。将基准测试模式配置为吞吐量模式，使用 @Warmup 注解配置预热次数为 10，使用 @OutputTimeUnit 指定输出单位为秒，使用 @Fork 指定进程数为 1，使用 @Threads 指定线程数为 8。</p>
<p>doSomething 方法吞吐量测试结果如下：</p>
<pre><code class="language-text">Result &quot;com.alibaba.csp.sentinel.benchmark.SentinelEntryBenchmark.doSomething&quot;:
  300948.682 ±(99.9%) 33237.428 ops/s [Average]
  (min, avg, max) = (295869.456, 300948.682, 316089.624), stdev = 8631.655
  CI (99.9%): [267711.254, 334186.110] (assumes normal distribution)

</code></pre>
<p>最小 ops/s 为 295869.456，平均 ops/s 为 300948.682，最大 ops/s 为 316089.624。</p>
<p>doSomethingWithEntry 方法吞吐量测试结果如下：</p>
<pre><code class="language-text">Result &quot;com.alibaba.csp.sentinel.benchmark.SentinelEntryBenchmark.doSomethingWithEntry&quot;:
  309934.827 ±(99.9%) 98910.540 ops/s [Average]
  (min, avg, max) = (280835.799, 309934.827, 337712.803), stdev = 25686.753
  CI (99.9%): [211024.287, 408845.366] (assumes normal distribution)

</code></pre>
<p>最小 ops/s 为 280835.799，平均 ops/s 为 309934.827，最大 ops/s 为 337712.803。</p>
<blockquote>
<p>OPS：每秒执行的操作次数，或每秒执行的方法次数。</p>
</blockquote>
<p>从本次测试结果可以看出，doSomething 方法的平均吞吐量与 doSomethingWithEntry 方法平均吞吐量相差约为 3%，也就是说，在超过 28w OPS（QPS）的情况下，Sentinel 对应用性能的影响只有 3%不到。实际项目场景，一个服务节点所有接口总的 QPS 也很难达到 25W 这个值，而 QPS 越低，Sentinel 对应用性能的影响也越低。</p>
<p>但这毕竟是在没有配置任何限流规则的情况下，只有一个资源且调用链路的深度（调用树的深度）为 1 的情况下，这个结果只能算个理想的参考值，还是以实际项目中的使用测试为准。</p>
<h3>总结</h3>
<p>到此，我们基本把 Sentinel 的核心实现源码大致都分析了一遍。我们也能从 Sentinel 源码的一些细节上看出 Sentinel 为性能所作出的努力，并也使用 JMH 对 Sentinel 做了一次简单的基准测试，得出 Sentinel 对应用性能影响非常小结论。</p>
<p>Sentinel 支持丰富的流控功能、扩展性极强，以及性能方面的优势，才是 Sentinel 被广泛使用的原因。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="19&#32;Sentinel&#32;集群限流的实现（下）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="21&#32;番外篇：Sentinel&#32;1.8.0&#32;熔断降级新特性解读.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43599d4cb6645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
