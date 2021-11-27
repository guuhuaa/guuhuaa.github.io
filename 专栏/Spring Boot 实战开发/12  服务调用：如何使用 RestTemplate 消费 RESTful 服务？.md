<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>12  服务调用：如何使用 RestTemplate 消费 RESTful 服务？.md</title>
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

                    <a class="current-tab" href="12&#32;&#32;服务调用：如何使用&#32;RestTemplate&#32;消费&#32;RESTful&#32;服务？.md">12  服务调用：如何使用 RestTemplate 消费 RESTful 服务？.md</a>
                    

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

                    
                    <a href="21&#32;&#32;指标定制：如何实现自定义度量指标和&#32;Actuator&#32;端点？.md">21  指标定制：如何实现自定义度量指标和 Actuator 端点？.md</a>

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
                        <div><h1>12  服务调用：如何使用 RestTemplate 消费 RESTful 服务？</h1>
<p>11 讲我们介绍了如何使用 Spring Boot 构建 RESTful 风格 Web 服务的实现方法，而 SpringCSS 案例系统的演进过程也从单个服务上升到多个服务之间的交互。</p>
<p>完成 Web 服务的构建后，我们需要做的事情就是如何对服务进行消费，这也是 12讲我们介绍的要点，接下来我们将基于 RestTemplate 模板工具类来完成这一目标。</p>
<h3>使用 RestTemplate 访问 HTTP 端点</h3>
<p>RestTemplate 是 Spring 提供的用于访问 RESTful 服务的客户端的模板工具类，它位于 org.springframework.web.client 包下。</p>
<p>在设计上，RestTemplate 完全可以满足 11 讲中介绍的 RESTful 架构风格的设计原则。相较传统 Apache 中的 HttpClient 客户端工具类，RestTemplate 在编码的简便性以及异常的处理等方面都做了很多改进。</p>
<p>接下来，我们先来看一下如何创建一个 RestTemplate 对象，并通过该对象所提供的大量工具方法实现对远程 HTTP 端点的高效访问。</p>
<h4>创建 RestTemplate</h4>
<p>如果我们想创建一个 RestTemplate 对象，最简单且最常见的方法是直接 new 一个该类的实例，如下代码所示：</p>
<pre><code>@Bean

public RestTemplate restTemplate(){

    return new RestTemplate();

}
</code></pre>
<p>这里我们创建了一个 RestTemplate 实例，并通过 @Bean 注解将其注入 Spring 容器中。</p>
<p>通常，我们会把上述代码放在 Spring Boot 的 Bootstrap 类中，使得我们在代码工程的其他地方也可以引用这个实例。</p>
<p>下面我们查看下 RestTemplate 的无参构造函数，看看创建它的实例时，RestTemplate 都做了哪些事情，如下代码所示：</p>
<pre><code>public RestTemplate() {

        this.messageConverters.add(new ByteArrayHttpMessageConverter());

        this.messageConverters.add(new StringHttpMessageConverter());

        this.messageConverters.add(new ResourceHttpMessageConverter(false));

        this.messageConverters.add(new SourceHttpMessageConverter&lt;&gt;());

        this.messageConverters.add(new AllEncompassingFormHttpMessageConverter());

 

        //省略其他添加 HttpMessageConverter 的代码

}
</code></pre>
<p><strong>可以看到 RestTemplate 的无参构造函数只做了一件事情，添加了一批用于实现消息转换的 HttpMessageConverter 对象。</strong></p>
<p>我们知道通过 RestTemplate 发送的请求和获取的响应都是以 JSON 作为序列化方式，而我们调用后续将要介绍的 getForObject、exchange 等方法时所传入的参数及获取的结果都是普通的 Java 对象，我们就是通过使用 RestTemplate 中的 HttpMessageConverter 自动帮我们做了这一层转换操作。</p>
<p><strong>这里请注意，其实 RestTemplate 还有另外一个更强大的有参构造函数</strong>，如下代码所示：</p>
<pre><code>public RestTemplate(ClientHttpRequestFactory requestFactory) {

        this();

        setRequestFactory(requestFactory);

}
</code></pre>
<p>从以上代码中，我们可以看到这个构造函数一方面调用了前面的无参构造函数，另一方面可以设置一个 ClientHttpRequestFactory 接口。而基于这个 ClientHttpRequestFactory 接口的各种实现类，我们可以对 RestTemplate 中的行为进行精细化控制。</p>
<p>这方面典型的应用场景是设置 HTTP 请求的超时时间等属性，如下代码所示：</p>
<pre><code>@Bean

public RestTemplate customRestTemplate(){

        HttpComponentsClientHttpRequestFactory httpRequestFactory = new HttpComponentsClientHttpRequestFactory();

        httpRequestFactory.setConnectionRequestTimeout(3000);

        httpRequestFactory.setConnectTimeout(3000);

        httpRequestFactory.setReadTimeout(3000);

 

        return new RestTemplate(httpRequestFactory);

}
</code></pre>
<p>这里我们创建了一个 HttpComponentsClientHttpRequestFactory 工厂类，它是 ClientHttpRequestFactory 接口的一个实现类。通过设置连接请求超时时间 ConnectionRequestTimeout、连接超时时间 ConnectTimeout 等属性，我们对 RestTemplate 的默认行为进行了定制化处理。</p>
<h4>使用 RestTemplate 访问 Web 服务</h4>
<p>在远程服务访问上，RestTemplate 内置了一批常用的工具方法，我们可以根据 HTTP 的语义以及 RESTful 的设计原则对这些工具方法进行分类，如下表所示。</p>
<p><img src="assets/CgqCHl_lfhWAWs-DAACna_DO-CA750.png" alt="Lark20201225-135202.png" /></p>
<p>RestTemplate 中的方法分类表</p>
<p>接下来，我们将基于该表对 RestTemplate 中的工具方法进行详细介绍并给出相关示例。不过在此之前，我们想先来讨论一下请求的 URL。</p>
<p>在一个 Web 请求中，我们可以通过请求路径携带参数。在使用 RestTemplate 时，我们也可以在它的 URL 中嵌入路径变量，示例代码如下所示：</p>
<pre><code>(&quot;http://localhost:8082/account/{id}&quot;, 1)
</code></pre>
<p>这里我们对 account-service 提供的一个端点进行了参数设置：我们定义了一个拥有路径变量名为 id 的 URL，实际访问时，我们将该变量值设置为 1。其实，在URL 中也可以包含多个路径变量，因为 Java 支持不定长参数语法，多个路径变量的赋值可以按照参数依次设置。</p>
<p>如下所示的代码中，我们在 URL 中使用了 pageSize 和 pageIndex 这两个路径变量进行分页操作，实际访问时它们将被替换为 20 和 2。</p>
<pre><code>(&quot;http://localhost:8082/account/{pageSize}/{pageIndex}&quot;, 20, 2)
</code></pre>
<p>而路径变量也可以通过 Map 进行赋值。如下所示的代码同样定义了拥有路径变量 pageSize 和 pageIndex 的 URL，但实际访问时，我们会从 uriVariables 这个 Map 对象中获取值进行替换，从而得到最终的请求路径为<a href="http://localhost:8082/account/20/2">http://localhost:8082/account/20/2</a>。</p>
<pre><code>Map&lt;String, Object&gt; uriVariables = new HashMap&lt;&gt;();

uriVariables.put(&quot;pageSize&quot;, 20);

uriVariables.put(&quot;pageIndex&quot;, 2);

webClient.getForObject() (&quot;http://localhost:8082/account/{pageSize}/{pageIndex}&quot;, Account.class, uriVariables);
</code></pre>
<p>请求 URL 一旦准备好了，我们就可以使用 RestTemplates 所提供的一系列工具方法完成远程服务的访问。</p>
<p>我们先来介绍 get 方法组，它包括 getForObject 和 getForEntity 这两组方法，每组各有三个方法。</p>
<p>例如，getForObject 方法组中的三个方法如下代码所示：</p>
<pre><code>public &lt;T&gt; T getForObject(URI url, Class&lt;T&gt; responseType)

public &lt;T&gt; T getForObject(String url, Class&lt;T&gt; responseType, Object... uriVariables){}

public &lt;T&gt; T getForObject(String url, Class&lt;T&gt; responseType, Map&lt;String, ?&gt; uriVariables)
</code></pre>
<p>从以上方法定义上，我们不难看出它们之间的区别只是传入参数的处理方式不同。</p>
<p>这里，我们注意到第一个 getForObject 方法只有两个参数（后面的两个 getForObject 方法分别支持不定参数以及一个 Map 对象），如果我们想在访问路径上添加一个参数，则需要我们构建一个独立的 URI 对象，示例如下代码所示：</p>
<pre><code>String url = &quot;http://localhost:8080/hello?name=&quot; + URLEncoder.encode(name, &quot;UTF-8&quot;);

URI uri = URI.create(url);
</code></pre>
<p>我们先来回顾下 12 讲中我们介绍的 AccountController，如下代码所示：</p>
<pre><code>@RestController

@RequestMapping(value = &quot;accounts&quot;)

public class AccountController {

 

    @GetMapping(value = &quot;/{accountId}&quot;)

    public Account getAccountById(@PathVariable(&quot;accountId&quot;) Long accountId) {

	…

    }

}
</code></pre>
<p>对于上述端点，我们可以通过 getForObject 方法构建一个 HTTP 请求来获取目标 Account 对象，实现代码如下所示：</p>
<pre><code>Account result = restTemplate.getForObject(&quot;http://localhost:8082/accounts/{accountId}&quot;, Account.class, accountId);
</code></pre>
<p>当然，我们也可以使用 getForEntity 方法实现同样的效果，但在写法上会有所区别，如下代码所示：</p>
<pre><code>ResponseEntity&lt;Account&gt; result = restTemplate.getForEntity(&quot;http://localhost:8082/accounts/{accountId}&quot;, Account.class, accountId);

Account account = result.getBody();
</code></pre>
<p>在以上代码中，我们可以看到 getForEntity 方法的返回值是一个 ResponseEntity 对象，在这个对象中还包含了 HTTP 消息头等信息，而 getForObject 方法返回的只是业务对象本身。这是这两个方法组的主要区别，你可以根据个人需要自行选择。</p>
<p><strong>与 GET 请求相比，RestTemplate 中的 POST 请求除提供了 postForObject 和 postForEntity 方法组以外，还额外提供了一组 postForLocation 方法。</strong></p>
<p>假设我们有如下所示的 OrderController ，它暴露了一个用于添加 Order 的端点。</p>
<pre><code>@RestController

@RequestMapping(value=&quot;orders&quot;)

public class OrderController {

 

    @PostMapping(value = &quot;&quot;)

    public Order addOrder(@RequestBody Order order) {

        Order result = orderService.addOrder(order);

         return result;

    }

}
</code></pre>
<p>那么，通过 postForEntity 发送 POST 请求的示例如下代码所示：</p>
<pre><code>Order order = new Order();

order.setOrderNumber(&quot;Order0001&quot;);

order.setDeliveryAddress(&quot;DemoAddress&quot;);

ResponseEntity&lt;Order&gt; responseEntity = restTemplate.postForEntity(&quot;http://localhost:8082/orders&quot;, order, Order.class);

return responseEntity.getBody();
</code></pre>
<p>从以上代码中可以看到，这里我们构建了一个 Order 实体，通过 postForEntity 传递给了 OrderController 所暴露的端点，并获取了该端点的返回值。<strong>（特殊说明：postForObject 的操作方式也与此类似。）</strong></p>
<p>掌握了 get 和 post 方法组后，理解 put 方法组和 delete 方法组就会非常容易了。其中 put 方法组与 post 方法组相比只是操作语义上的差别，而 delete 方法组的使用过程也和 get 方法组类似。这里我们就不再一一展开，你可以自己尝试做一些练习。</p>
<p>最后，我们还有必要介绍下 exchange 方法组。</p>
<p><strong>对于 RestTemplate 而言，exchange 是一个通用且统一的方法，它既能发送 GET 和 POST 请求，也能用于发送其他各种类型的请求。</strong></p>
<p>我们来看下 exchange 方法组中的其中一个方法签名，如下代码所示：</p>
<pre><code>public &lt;T&gt; ResponseEntity&lt;T&gt; exchange(String url, HttpMethod method, @Nullable HttpEntity&lt;?&gt; requestEntity, Class&lt;T&gt; responseType, Object... uriVariables) throws RestClientException
</code></pre>
<p><strong>请注意，这里的 requestEntity 变量是一个 HttpEntity 对象，它封装了请求头和请求体，而 responseType 用于指定返回数据类型。</strong> 假如前面的 OrderController 中存在一个根据订单编号 OrderNumber 获取 Order 信息的端点，那么我们使用 exchange 方法发起请求的代码就变成这样了，如下代码所示。</p>
<pre><code>ResponseEntity&lt;Order&gt; result = restTemplate.exchange(&quot;http://localhost:8082/orders/{orderNumber}&quot;, HttpMethod.GET, null, Order.class, orderNumber);
</code></pre>
<p>而比较复杂的一种使用方式是分别设置 HTTP 请求头及访问参数，并发起远程调用，示例代码如下所示：</p>
<pre><code>//设置 HTTP Header

HttpHeaders headers = new HttpHeaders();

headers.setContentType(MediaType.APPLICATION_JSON_UTF8);

 

//设置访问参数

HashMap&lt;String, Object&gt; params = new HashMap&lt;&gt;();

params.put(&quot;orderNumber&quot;, orderNumber);

 

//设置请求 Entity

HttpEntity entity = new HttpEntity&lt;&gt;(params, headers);

ResponseEntity&lt;Order&gt; result = restTemplate.exchange(url, HttpMethod.GET, entity, Order.class);
</code></pre>
<h4>RestTemplate 其他使用技巧</h4>
<p>除了实现常规的 HTTP 请求，RestTemplate 还有一些高级用法可供我们进行使用，如指定消息转换器、设置拦截器和处理异常等。</p>
<p><strong>指定消息转换器</strong></p>
<p>在 RestTemplate 中，实际上还存在第三个构造函数，如下代码所示：</p>
<pre><code>public RestTemplate(List&lt;HttpMessageConverter&lt;?&gt;&gt; messageConverters) {

        Assert.notEmpty(messageConverters, &quot;At least one HttpMessageConverter required&quot;);

        this.messageConverters.addAll(messageConverters);

}
</code></pre>
<p>从以上代码中不难看出，我们可以通过传入一组 HttpMessageConverter 来初始化 RestTemplate，这也为消息转换器的定制提供了途径。</p>
<p>假如，我们希望把支持 Gson 的 GsonHttpMessageConverter 加载到 RestTemplate 中，就可以使用如下所示的代码。</p>
<pre><code>@Bean

public RestTemplate restTemplate() {

        List&lt;HttpMessageConverter&lt;?&gt;&gt; messageConverters = new ArrayList&lt;HttpMessageConverter&lt;?&gt;&gt;();

        messageConverters.add(new GsonHttpMessageConverter());

        RestTemplate restTemplate = new RestTemplate(messageConverters);

        return restTemplate;

}
</code></pre>
<p>原则上，我们可以根据需要实现各种自定义的 HttpMessageConverter ，并通过以上方法完成对 RestTemplate 的初始化。</p>
<p><strong>设置拦截器</strong></p>
<p>如果我们想对请求做一些通用拦截设置，那么我们可以使用拦截器。不过，使用拦截器之前，首先我们需要实现 ClientHttpRequestInterceptor 接口。</p>
<p>这方面最典型的应用场景是在 Spring Cloud 中通过 @LoadBalanced 注解为 RestTemplate 添加负载均衡机制。我们可以在 LoadBalanceAutoConfiguration 自动配置类中找到如下代码。</p>
<pre><code>@Bean

@ConditionalOnMissingBean

public RestTemplateCustomizer restTemplateCustomizer(

            final LoadBalancerInterceptor loadBalancerInterceptor) {

        return restTemplate -&gt; {

            List&lt;ClientHttpRequestInterceptor&gt; list = new ArrayList&lt;&gt;(

                    restTemplate.getInterceptors());

            list.add(loadBalancerInterceptor);

            restTemplate.setInterceptors(list);

        };

}
</code></pre>
<p>在上面代码中，我们可以看到这里出现了一个 LoadBalancerInterceptor 类，该类实现了 ClientHttpRequestInterceptor 接口，然后我们通过调用 setInterceptors 方法将这个自定义的 LoadBalancerInterceptor 注入 RestTemplate 的拦截器列表中。</p>
<p><strong>处理异常</strong></p>
<p>请求状态码不是返回 200 时，RestTemplate 在默认情况下会抛出异常，并中断接下来的操作，如果我们不想采用这个处理过程，那么就需要覆盖默认的 ResponseErrorHandler。示例代码结构如下所示：</p>
<pre><code>RestTemplate restTemplate = new RestTemplate();

 

ResponseErrorHandler responseErrorHandler = new ResponseErrorHandler() {

        @Override

        public boolean hasError(ClientHttpResponse clientHttpResponse) throws IOException {

            return true;

        }

 

        @Override

        public void handleError(ClientHttpResponse clientHttpResponse) throws IOException {

            //添加定制化的异常处理代码

        }

};

 

restTemplate.setErrorHandler(responseErrorHandler);
</code></pre>
<p>在上述的 handleError 方法中，我们可以实现任何自己想控制的异常处理代码。</p>
<h3>实现 SpringCSS 案例中的服务交互</h3>
<p>介绍完 RestTemplate 模板工具类的使用方式后，我们再回到 SpringCSS 案例。</p>
<p>11 讲中，我们已经给出了 customer-service 的 CustomerService 类中用于完成与 account-service 和 order-service 进行集成的 generateCustomerTicket 方法的代码结构，如下代码所示：</p>
<pre><code>public CustomerTicket generateCustomerTicket(Long accountId, String orderNumber) {

        // 创建客服工单对象

        CustomerTicket customerTicket = new CustomerTicket();

 

        // 从远程 account-service 中获取 Account 对象

        Account account = getRemoteAccountById(accountId);

 

        // 从远程 order-service 中获取 Order 读写

        Order order = getRemoteOrderByOrderNumber(orderNumber);

        // 设置 CustomerTicket 对象并保存

        customerTicket.setAccountId(accountId);

        customerTicket.setOrderNumber(order.getOrderNumber());

        customerTicketRepository.save(customerTicket);

 

        return customerTicket;

}
</code></pre>
<p>这里以 getRemoteOrderByOrderNumber 方法为例，我们来对它的实现过程进行展开，getRemoteOrderByOrderNumber 方法定义代码如下：</p>
<pre><code>@Autowired

private OrderClient orderClient;

 

private OrderMapper getRemoteOrderByOrderNumber(String orderNumber) {

 

        return orderClient.getOrderByOrderNumber(orderNumber);

}
</code></pre>
<p>getRemoteAccountById 方法的实现过程也类似。</p>
<p>接下来我们构建一个 OrderClient 类完成对 order-service 的远程访问，如下代码所示：</p>
<pre><code>@Component

public class OrderClient {

 

    private static final Logger logger = LoggerFactory.getLogger(OrderClient.class);

 

    @Autowired

    RestTemplate restTemplate;

 

    public OrderMapper getOrderByOrderNumber(String orderNumber) {

 

        logger.debug(&quot;Get order from remote: {}&quot;, orderNumber);

 

        ResponseEntity&lt;OrderMapper&gt; result = restTemplate.exchange(

                &quot;http://localhost:8083/orders/{orderNumber}&quot;, HttpMethod.GET, null,

                OrderMapper.class, orderNumber);

 

         OrderMapper order= result.getBody();

 

        return order;

    }

}
</code></pre>
<p><strong>注意：这里我们注入了一个 RestTemplate 对象，并通过它的 exchange 方法完成对远程 order-serivce 的请求过程。且这里的返回对象是一个 OrderMapper，而不是一个 Order 对象。最后，RestTemplate 内置的 HttpMessageConverter 完成 OrderMapper 与 Order 之间的自动映射。</strong></p>
<p>事实上，OrderMapper 与 Order 对象的内部字段一一对应，它们分别位于两个不同的代码工程中，为了以示区别我们才故意在命名上做了区分。</p>
<h3>小结与预告</h3>
<p>12 讲的内容，我们是在 11 讲的内容基础上引入了 RestTemplate 模板类来完成对远程 HTTP 端点的访问。RestTemplate 为开发人员提供了一大批有用的工具方法来实现 HTTP 请求的发送以及响应的获取。同时，该模板类还开发了一些定制化的入口供开发人员嵌入，用来实现对 HTTP 请求过程进行精细化管理的处理逻辑。和 JdbcTemplate 一样，RestTemplate 在设计和实现上也是一款非常有效的工具类。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="11&#32;&#32;服务发布：如何构建一个&#32;RESTful&#32;风格的&#32;Web&#32;服务？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="13&#32;&#32;服务调用：如何正确理解&#32;RestTemplate&#32;远程调用实现原理？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434d212ec270ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
