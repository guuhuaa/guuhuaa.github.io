<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>21  指标定制：如何实现自定义度量指标和 Actuator 端点？.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;从零开始：为什么要学习&#32;Spring&#32;Boot？.md">00 开篇词  从零开始：为什么要学习 Spring Boot？.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;家族生态：如何正确理解&#32;Spring&#32;家族的技术体系？.md">01  家族生态：如何正确理解 Spring 家族的技术体系？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;案例驱动：如何剖析一个&#32;Spring&#32;Web&#32;应用程序？.md">02  案例驱动：如何剖析一个 Spring Web 应用程序？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;多维配置：如何使用&#32;Spring&#32;Boot&#32;中的配置体系？.md">03  多维配置：如何使用 Spring Boot 中的配置体系？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;定制配置：如何创建和管理自定义的配置信息？.md">04  定制配置：如何创建和管理自定义的配置信息？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;自动配置：如何正确理解&#32;Spring&#32;Boot&#32;自动配置实现原理？.md">05  自动配置：如何正确理解 Spring Boot 自动配置实现原理？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;基础规范：如何理解&#32;JDBC&#32;关系型数据库访问规范？.md">06  基础规范：如何理解 JDBC 关系型数据库访问规范？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;数据访问：如何使用&#32;JdbcTemplate&#32;访问关系型数据库？.md">07  数据访问：如何使用 JdbcTemplate 访问关系型数据库？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;数据访问：如何剖析&#32;JdbcTemplate&#32;数据访问实现原理？.md">08  数据访问：如何剖析 JdbcTemplate 数据访问实现原理？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;数据抽象：Spring&#32;Data&#32;如何对数据访问过程进行统一抽象？.md">09  数据抽象：Spring Data 如何对数据访问过程进行统一抽象？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;ORM&#32;集成：如何使用&#32;Spring&#32;Data&#32;JPA&#32;访问关系型数据库？.md">10  ORM 集成：如何使用 Spring Data JPA 访问关系型数据库？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;服务发布：如何构建一个&#32;RESTful&#32;风格的&#32;Web&#32;服务？.md">11  服务发布：如何构建一个 RESTful 风格的 Web 服务？.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;服务调用：如何使用&#32;RestTemplate&#32;消费&#32;RESTful&#32;服务？.md">12  服务调用：如何使用 RestTemplate 消费 RESTful 服务？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;服务调用：如何正确理解&#32;RestTemplate&#32;远程调用实现原理？.md">13  服务调用：如何正确理解 RestTemplate 远程调用实现原理？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;消息驱动：如何使用&#32;KafkaTemplate&#32;集成&#32;Kafka？.md">14  消息驱动：如何使用 KafkaTemplate 集成 Kafka？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;消息驱动：如何使用&#32;JmsTemplate&#32;集成&#32;ActiveMQ？.md">15  消息驱动：如何使用 JmsTemplate 集成 ActiveMQ？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;消息驱动：如何使用&#32;RabbitTemplate&#32;集成&#32;RabbitMQ？.md">16  消息驱动：如何使用 RabbitTemplate 集成 RabbitMQ？.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;安全架构：如何理解&#32;Spring&#32;安全体系的整体架构？.md">17  安全架构：如何理解 Spring 安全体系的整体架构？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;用户认证：如何基于&#32;Spring&#32;Security&#32;构建用户认证体系？.md">18  用户认证：如何基于 Spring Security 构建用户认证体系？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;服务授权：如何基于&#32;Spring&#32;Security&#32;确保请求安全访问？.md">19  服务授权：如何基于 Spring Security 确保请求安全访问？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;服务监控：如何使用&#32;Actuator&#32;组件实现系统监控？.md">20  服务监控：如何使用 Actuator 组件实现系统监控？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="21&#32;&#32;指标定制：如何实现自定义度量指标和&#32;Actuator&#32;端点？.md">21  指标定制：如何实现自定义度量指标和 Actuator 端点？.md</a>
                    

                </li>
                <li>

                    
                    <a href="22&#32;&#32;运行管理：如何使用&#32;Admin&#32;Server&#32;管理&#32;Spring&#32;应用程序？.md">22  运行管理：如何使用 Admin Server 管理 Spring 应用程序？.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;数据测试：如何使用&#32;Spring&#32;测试数据访问层组件？.md">23  数据测试：如何使用 Spring 测试数据访问层组件？.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;服务测试：如何使用&#32;Spring&#32;测试&#32;Web&#32;服务层组件？.md">24  服务测试：如何使用 Spring 测试 Web 服务层组件？.md</a>

                </li>
                <li>

                    
                    <a href="结束语&#32;&#32;以终为始：Spring&#32;Boot&#32;总结和展望.md">结束语  以终为始：Spring Boot 总结和展望.md</a>

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
                        <div><h1>21  指标定制：如何实现自定义度量指标和 Actuator 端点？</h1>
<p>20 讲中我们引入了 Spring Boot Actuator 组件来满足 Spring Boot 应用程序的系统监控功能，并重点介绍了如何扩展常见的 Info 和 Health 监控端点的实现方法。</p>
<p>这一讲我们继续讨论如何扩展 Actuator 端点，但更多关注与度量指标相关的内容。同时，我们还将给出如何创建自定义 Actuator 的实现方法，以便应对默认端点无法满足需求的应用场景。</p>
<h3>Actuator 中的度量指标</h3>
<p><strong>对于系统监控而言，度量是一个很重要的维度。</strong> 在 Spring Boot 2.X 版本中，Actuator 组件主要使用内置的 Micrometer 库实现度量指标的收集和分析。</p>
<h4>Micrometer 度量库</h4>
<p>Micrometer 是一款监控指标的度量类库，为 Java 平台上的性能数据收集提供了一套通用的 API。在应用程序中，我们只使用 Micrometer 提供的通用 API 即可收集度量指标。</p>
<p>下面我们先来简要介绍 Micrometer 中包含的几个核心概念。</p>
<p>首先我们需要介绍的是计量器 Meter，它是一个接口，代表的是需要收集的性能指标数据。关于 Meter 的定义如下：</p>
<pre><code>public interface Meter extends AutoCloseable {

   

    //Meter 的唯一标识，是名称和标签的一种组合

    Id getId();

 

    //一组测量结果

	Iterable&lt;Measurement&gt; measure();

	 

	//Meter 的类型枚举值

    enum Type {

        COUNTER,

        GAUGE,

        LONG_TASK_TIMER,

        TIMER,

        DISTRIBUTION_SUMMARY,

        OTHER

    }

}
</code></pre>
<p>通过上述代码，我们注意到 Meter 中存在一个 Id 对象，该对象的作用是定义 Meter 的名称和标签。从 Type 的枚举值中，我们不难看出 Micrometer 中包含的所有计量器类型。</p>
<p>接下来我们先说明两个概念。</p>
<blockquote>
<p><strong>Meter 的名称</strong>：对于计量器来说，每个计量器都有自己的名称，而且在创建时它们都可以指定一系列标签。
<strong>Meter 的标签</strong>：标签的作用在于监控系统可以通过这些标签对度量进行分类过滤。</p>
</blockquote>
<p><strong>在日常开发过程中，常用的计量器类型主要分为计数器 Counter、计量仪 Gauge 和计时器 Timer 这三种。</strong></p>
<ul>
<li><strong>Counter</strong>：这个计量器的作用和它的名称一样，就是一个不断递增的累加器，我们可以通过它的 increment 方法实现累加逻辑。</li>
<li><strong>Gauge</strong>：与 Counter 不同，Gauge 所度量的值并不一定是累加的，我们可以通过它的 gauge 方法指定数值。</li>
<li><strong>Timer</strong>：这个计量器比较简单，就是用来记录事件的持续时间。</li>
</ul>
<p>既然我们已经明确了常用的计量器及其使用场景，那么如何创建这些计量器呢？</p>
<p>在 Micrometer 中，我们提供了一个计量器注册表 MeterRegistry，它主要负责创建和维护各种计量器。关于 MeterRegistry 的创建方法如下代码所示：</p>
<pre><code>public abstract class MeterRegistry implements AutoCloseable {

 

    protected abstract &lt;T&gt; Gauge newGauge(Meter.Id id, @Nullable T obj, ToDoubleFunction&lt;T&gt; valueFunction);

 

    protected abstract Counter newCounter(Meter.Id id);

 

    protected abstract Timer newTimer(Meter.Id id, DistributionStatisticConfig distributionStatisticConfig, PauseDetector pauseDetector);

…

}
</code></pre>
<p>以上代码只是创建 Meter 的一种途径，从中我们可以看到 MeterRegistry 针对不同的 Meter 提供了对应的创建方法。</p>
<p>而创建 Meter 的另一种途径是使用某个 Meter 的具体 builder 方法。以 Counter 为例，它的定义中包含了一个 builder 方法和一个 register 方法，如下代码所示：</p>
<pre><code>public interface Counter extends Meter {

    static Builder builder(String name) {

        return new Builder(name);

	}

	 

    default void increment() {

        increment(1.0);

	}

	 

	void increment(double amount);

	 

	double count();

 

    @Override

    default Iterable&lt;Measurement&gt; measure() {

        return Collections.singletonList(new Measurement(this::count, Statistic.COUNT));

	}

         …

 

    public Counter register(MeterRegistry registry) {

        return registry.counter(new Meter.Id(name, tags, baseUnit, description, Type.COUNTER));

    }

}
</code></pre>
<p>注意到最后的 register 方法就是将当前的 Counter 注册到 MeterRegistry 中，因此我们需要创建一个 Counter。通常，我们会采用如下所示代码进行创建。</p>
<pre><code>Counter counter = Counter.builder(&quot;counter1&quot;)

        .tag(&quot;tag1&quot;, &quot;value1&quot;)

        .register(registry);
</code></pre>
<p>了解了 Micrometer 框架的基本概念后，接下来我们回到 Spring Boot Actuator，一起来看看它提供的专门针对度量指标管理的 Metrics 端点。</p>
<h4>扩展 Metrics 端点</h4>
<p>在 Spring Boot 中，它为我们提供了一个 Metrics 端点用于实现生产级的度量工具。访问 actuator/metrics 端点后，我们将得到如下所示的一系列度量指标。</p>
<pre><code>{

     &quot;names&quot;:[

         &quot;jvm.memory.max&quot;,

         &quot;jvm.threads.states&quot;,

         &quot;jdbc.connections.active&quot;,

         &quot;jvm.gc.memory.promoted&quot;,

         &quot;jvm.memory.used&quot;,

         &quot;jvm.gc.max.data.size&quot;,

         &quot;jdbc.connections.max&quot;,

         &quot;jdbc.connections.min&quot;,

         &quot;jvm.memory.committed&quot;,

         &quot;system.cpu.count&quot;,

         &quot;logback.events&quot;,

         &quot;http.server.requests&quot;,

         &quot;jvm.buffer.memory.used&quot;,

         &quot;tomcat.sessions.created&quot;,

         &quot;jvm.threads.daemon&quot;,

         &quot;system.cpu.usage&quot;,

         &quot;jvm.gc.memory.allocated&quot;,

         &quot;hikaricp.connections.idle&quot;,

         &quot;hikaricp.connections.pending&quot;,

         &quot;jdbc.connections.idle&quot;,

         &quot;tomcat.sessions.expired&quot;,

         &quot;hikaricp.connections&quot;,

         &quot;jvm.threads.live&quot;,

         &quot;jvm.threads.peak&quot;,

         &quot;hikaricp.connections.active&quot;,

         &quot;hikaricp.connections.creation&quot;,

         &quot;process.uptime&quot;,

         &quot;tomcat.sessions.rejected&quot;,

         &quot;process.cpu.usage&quot;,

         &quot;jvm.classes.loaded&quot;,

         &quot;hikaricp.connections.max&quot;,

         &quot;hikaricp.connections.min&quot;,

         &quot;jvm.gc.pause&quot;,

         &quot;jvm.classes.unloaded&quot;,

         &quot;tomcat.sessions.active.current&quot;,

         &quot;tomcat.sessions.alive.max&quot;,

         &quot;jvm.gc.live.data.size&quot;,

         &quot;hikaricp.connections.usage&quot;,

         &quot;hikaricp.connections.timeout&quot;,

         &quot;jvm.buffer.count&quot;,

         &quot;jvm.buffer.total.capacity&quot;,

         &quot;tomcat.sessions.active.max&quot;,

         &quot;hikaricp.connections.acquire&quot;,

         &quot;process.start.time&quot;

     ]

 }
</code></pre>
<p>以上代码中涉及的指标包括常规的系统内存总量、空闲内存数量、处理器数量、系统正常运行时间、堆信息等，也包含我们引入 JDBC 和 HikariCP 数据源组件之后的数据库连接信息等。此时，如果我们想了解某项指标的详细信息，在 actuator/metrics 端点后添加对应指标的名称即可。</p>
<p>例如我们想了解当前内存的使用情况，就可以通过 actuator/metrics/jvm.memory.used 端点进行获取，如下代码所示。</p>
<pre><code>{

     &quot;name&quot;:&quot;jvm.memory.used&quot;,

     &quot;description&quot;:&quot;The amount of used memory&quot;,

     &quot;baseUnit&quot;:&quot;bytes&quot;,

     &quot;measurements&quot;:[

         {

             &quot;statistic&quot;:&quot;VALUE&quot;,

             &quot;value&quot;:115520544

         }

     ],

     &quot;availableTags&quot;:[

         {

             &quot;tag&quot;:&quot;area&quot;,

             &quot;values&quot;:[

                 &quot;heap&quot;,

                 &quot;nonheap&quot;

             ]

         },

         {

             &quot;tag&quot;:&quot;id&quot;,

             &quot;values&quot;:[

                 &quot;Compressed Class Space&quot;,

                 &quot;PS Survivor Space&quot;,

                 &quot;PS Old Gen&quot;,

                 &quot;Metaspace&quot;,

                 &quot;PS Eden Space&quot;,

                 &quot;Code Cache&quot;

             ]

         }

     ]

 }
</code></pre>
<p>前面介绍 Micrometer 时，我们已经提到 Metrics 指标体系中包含支持 Counter 和 Gauge 这两种级别的度量指标。通过将 <a href="https://github.com/spring-projects/spring-boot/blob/master/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/metrics/CounterService.java">Counter</a> 或 <a href="https://github.com/spring-projects/spring-boot/tree/master/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/metrics/GaugeService.java">Gauge </a>注入业务代码中，我们就可以记录自己想要的度量指标。其中，<a href="https://github.com/spring-projects/spring-boot/blob/master/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/metrics/CounterService.java">Counter</a> 用来暴露 increment() 方法，而 <a href="https://github.com/spring-projects/spring-boot/tree/master/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/metrics/GaugeService.java">Gauge</a> 用来提供一个 value() 方法。</p>
<p>下面我们以 Counter 为例介绍在业务代码中嵌入自定义 Metrics 指标的方法，如下代码所示：</p>
<pre><code>@Component

public class CounterService {

    

    public CounterService() {

        Metrics.addRegistry(new SimpleMeterRegistry());

    }

 

    public void counter(String name, String... tags) {

        Counter counter = Metrics.counter(name, tags);

        counter.increment();

    }

}
</code></pre>
<p>在这段代码中，我们构建了一个公共服务 CounterService，并开放了一个 Counter 方法供业务系统进行使用。当然，你也可以自己实现类似的工具类完成对各种计量器的封装。</p>
<p>另外，Micrometer 还提供了一个 MeterRegistry 工具类供我们创建度量指标。因此，我们也十分推荐使用 MeterRegistry 对各种自定义度量指标的创建过程进行简化。</p>
<h4>使用 MeterRegistry</h4>
<p>再次回到 SpringCSS 案例，此次我们来到 customer-service 的 CustomerTicketService 中。</p>
<p>比如我们希望系统每创建一个客服工单，就对所创建的工单进行计数，并作为系统运行时的一项度量指标，该效果的实现方式如下代码所示：</p>
<pre><code>@Service

public class CustomerTicketService {

    

    @Autowired

    private MeterRegistry meterRegistry;

 

public CustomerTicket generateCustomerTicket(Long accountId, String orderNumber) {

 

    CustomerTicket customerTicket = new CustomerTicket();

    …

        meterRegistry.summary(&quot;customerTickets.generated.count&quot;).record(1);

 

        return customerTicket;

    }   

}
</code></pre>
<p>在上述 generateCustomerTicket 方法中，通过 MeterRegistry 我们实现了每次创建 CustomerTicket 时自动添加一个计数的功能。</p>
<p>而且，MeterRegistry 还提供了一些类工具方法用于创建自定义度量指标。这些类工具方法除了常规的 counter、gauge、timer 等对应具体 Meter 的工具方法之外，还包括上述代码中的 summary 方法，且 Summary 方法返回的是一个 DistributionSummary 对象，关于它的定义如下代码所示：</p>
<pre><code>public interface DistributionSummary extends Meter, HistogramSupport {

 

    static Builder builder(String name) {

        return new Builder(name);

    }

    //记录数据

    void record(double amount);

 

    //记录操作执行的次数

    long count();

 

    //记录数据的数量

    double totalAmount();

 

    //记录数据的平均值

    default double mean() {

        return count() == 0 ? 0 : totalAmount() / count();

    }

 

    //记录数据的最大值

	double max();

	…

}
</code></pre>
<p>因为 DistributionSummary 的作用是记录一系列的事件并对这些事件进行处理，所以在 CustomerTicketService 中添加的meterRegistry.summary(&quot;customertickets.generated.count&quot;).record(1) 这行代码相当于每次调用 generateCustomerTicket 方法时，我们都会对这次调用进行记录。</p>
<p>现在访问 actuator/metrics/customertickets.generated.count 端点，我们就能看到如下所示的随着服务调用不断递增的度量信息。</p>
<pre><code>{

     &quot;name&quot;:&quot;customertickets.generated.count&quot;,

     &quot;measurements&quot;:[

         {

             &quot;statistic&quot;:&quot;Count&quot;,

             &quot;value&quot;:1

         },

         {

             &quot;statistic&quot;:&quot;Total&quot;,

             &quot;value&quot;:19

         }

     ] 

 }
</code></pre>
<p>显然，通过 MeterRegistry 实现自定义度量指标的使用方法更加简单。这里，你也可以结合业务需求尝试该类的不同功能。</p>
<p>接下来我们再来看一个相对比较复杂的使用方式。在 customer-service 中，我们同样希望系统存在一个度量值，该度量值用于记录所有新增的 CustomerTicket 个数，这次的示例代码如下所示：</p>
<pre><code>@Component

public class CustomerTicketMetrics extends AbstractRepositoryEventListener&lt;CustomerTicket&gt; {

 

    private MeterRegistry meterRegistry;

 

    public CustomerTicketMetrics(MeterRegistry meterRegistry) {

        this.meterRegistry = meterRegistry;

    }

 

    @Override

    protected void onAfterCreate(CustomerTicket customerTicket) {                 meterRegistry.counter(&quot;customerTicket.created.count&quot;).increment();  

	}

}
</code></pre>
<p>首先，这里我们使用了 MeterRegistry 的 Counter 方法初始化一个 counter，然后调用它的 increment 方法增加度量计数（这部分内容我们已经很熟悉了）。</p>
<p><strong>注意到这里，我们同时还引入了一个 AbstractRepositoryEventListener 抽象类，这个抽象类能够监控 Spring Data 中 Repository 层操作所触发的事件 RepositoryEvent，例如实体创建前后的 BeforeCreateEvent 和 AfterCreateEvent 事件、实体保存前后的 BeforeSaveEvent 和 AfterSaveEvent 事件等。</strong></p>
<p>针对这些事件，AbstractRepositoryEventListener 能捕捉并调用对应的回调函数。关于 AbstractRepositoryEventListener 类的部分实现如下代码所示：</p>
<pre><code>public abstract class AbstractRepositoryEventListener&lt;T&gt; implements ApplicationListener&lt;RepositoryEvent&gt; {

 

    public final void onApplicationEvent(RepositoryEvent event) {

        

        …

        Class&lt;?&gt; srcType = event.getSource().getClass();

        

        if (event instanceof BeforeSaveEvent) {

            onBeforeSave((T) event.getSource());

        } else if (event instanceof BeforeCreateEvent) {

            onBeforeCreate((T) event.getSource());

        } else if (event instanceof AfterCreateEvent) {

            onAfterCreate((T) event.getSource());

        } else if (event instanceof AfterSaveEvent) {

            onAfterSave((T) event.getSource());

              }

        …

	}

}
</code></pre>
<p>在这段代码中，我们可以看到 AbstractRepositoryEventListener 直接实现了 Spring 容器中的 ApplicationListener 监听器接口，并在 onApplicationEvent 方法中根据所传入的事件类型触发了回调函数。</p>
<p>以案例中的需求场景为例，我们可以在创建 Account 实体之后执行度量操作。也就是说，可以把度量操作的代码放在 onAfterCreate 回调函数中，正如案例代码中所展示那样。</p>
<p>现在我们执行生成客户工单操作，并访问对应的 Actuator 端点，同样可以看到度量数据在不断上升。</p>
<h3>自定义 Actuator 端点</h3>
<p>在日常开发过程中，扩展现有端点有时并不一定能满足业务需求，而自定义 Spring Boot Actuator 监控端点算是一种更灵活的方法。</p>
<p>假设我们需要提供一个监控端点以获取当前系统的用户信息和计算机名称，就可以通过一个独立的 MySystemEndPoint 进行实现，如下代码所示：</p>
<pre><code>@Configuration

@Endpoint(id = &quot;mysystem&quot;, enableByDefault=true)

public class MySystemEndpoint { 

 

    @ReadOperation

    public Map&lt;String, Object&gt; getMySystemInfo() {

        Map&lt;String,Object&gt; result= new HashMap&lt;&gt;();

        Map&lt;String, String&gt; map = System.getenv();

        result.put(&quot;username&quot;,map.get(&quot;USERNAME&quot;));

        result.put(&quot;computername&quot;,map.get(&quot;COMPUTERNAME&quot;));

        return result;

    }

}
</code></pre>
<p>在这段代码中我们可以看到，MySystemEndpoint 主要通过系统环境变量获取所需监控信息。</p>
<p>注意，这里我们引入了一个新的注解 @Endpoint，该注解定义如下代码所示：</p>
<pre><code>@Target(ElementType.TYPE)

@Retention(RetentionPolicy.RUNTIME)

@Documented

public @interface Endpoint {

 

    //端点 id

    String id() default &quot;&quot;;

 

    //是否默认启动标志位

    boolean enableByDefault() default true;

}
</code></pre>
<p>这段代码中的 @Endpoint 注解主要用于设置端点 id 及是否默认启动的标志位。且在案例中，我们指定了 id 为“mysystem”，enableByDefault 标志为 true。</p>
<p>事实上，在 Actuator 中也存在一批类似 @Endpoint 的端点注解。其中被 @Endpoint 注解的端点可以通过 JMX 和 Web 访问应用程序，对应的被 @JmxEndpoint 注解的端点只能通过 JMX 访问，而被 @WebEndpoint 注解的端点只能通过 Web 访问。</p>
<p>在示例代码中，我们还看到了一个 @ReadOperation 注解，该注解作用于方法，用于标识读取数据操作。<strong>在 Actuator 中，除了提供 @ReadOperation 注解之外，还提供 @WriteOperation 和 @DeleteOperation 注解，它们分别对应写入操作和删除操作。</strong></p>
<p>现在，通过访问 <a href="http://localhost:8080/">http://localhost:8080/</a>actuator/mysystem，我们就能获取如下所示监控信息。</p>
<pre><code>{

     &quot;computername&quot;:&quot;LAPTOP-EQB59J5P&quot;,

     &quot;username&quot;:&quot;user&quot;

 }
</code></pre>
<p>有时为了获取特定的度量信息，我们需要对某个端点传递参数，而 Actuator 专门提供了一个 @Selector 注解标识输入参数，示例代码如下所示：</p>
<pre><code>@Configuration

@Endpoint(id = &quot;account&quot;, enableByDefault = true)

public class AccountEndpoint {

    

    @Autowired

    private AccountRepository accountRepository;    

 

    @ReadOperation

    public Map&lt;String, Object&gt; getMySystemInfo(@Selector String arg0) {

        Map&lt;String, Object&gt; result = new HashMap&lt;&gt;();

        result.put(accountName, accountRepository.findAccountByAccountName(arg0));

        return result;

    }

}
</code></pre>
<p>这段代码的逻辑非常简单，就是根据传入的 accountName 获取用户账户信息。</p>
<p><strong>这里请注意，通过 @Selector 注解，我们就可以使用</strong><a href="http://localhost:8080/">http://localhost:8080/</a><strong>actuator/ account/account1 这样的端口地址触发度量操作了。</strong></p>
<h3>小结与预告</h3>
<p>度量是我们观测一个应用程序运行时状态的核心手段。这一讲我们介绍了 Spring Boot 中新引入的 Micrometer 度量库，以及该库中提供的各种度量组件。同时，我们还基于 Micrometer 中的核心工具类 MeterRegistry 完成了在业务系统中嵌入度量指标的实现过程。最后，我们还简要介绍了如何自定义一个 Actuator 端点的开发方法。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="20&#32;&#32;服务监控：如何使用&#32;Actuator&#32;组件实现系统监控？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="22&#32;&#32;运行管理：如何使用&#32;Admin&#32;Server&#32;管理&#32;Spring&#32;应用程序？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434d5bcb5a70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Spring%20Boot%20%E5%AE%9E%E6%88%98%E5%BC%80%E5%8F%91/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
