<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>24  服务测试：如何使用 Spring 测试 Web 服务层组件？.md</title>
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

                    
                    <a href="21&#32;&#32;指标定制：如何实现自定义度量指标和&#32;Actuator&#32;端点？.md">21  指标定制：如何实现自定义度量指标和 Actuator 端点？.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;运行管理：如何使用&#32;Admin&#32;Server&#32;管理&#32;Spring&#32;应用程序？.md">22  运行管理：如何使用 Admin Server 管理 Spring 应用程序？.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;数据测试：如何使用&#32;Spring&#32;测试数据访问层组件？.md">23  数据测试：如何使用 Spring 测试数据访问层组件？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="24&#32;&#32;服务测试：如何使用&#32;Spring&#32;测试&#32;Web&#32;服务层组件？.md">24  服务测试：如何使用 Spring 测试 Web 服务层组件？.md</a>
                    

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
                        <div><h1>24  服务测试：如何使用 Spring 测试 Web 服务层组件？</h1>
<p>23 讲我们介绍了对数据访问层进行测试的方法，这一讲将着重介绍对三层架构中的另外两层（Service 层和 Controller 层）的测试方法。</p>
<p>与位于底层的数据访问层不同，这两层的组件都依赖于它的下一层组件，即 Service 层依赖于数据访问层，而 Controller 层依赖于 Service 层。因此，对这两层进行测试时，我们将使用不同的方案和技术。</p>
<h3>使用 Environment 测试配置信息</h3>
<p>在《定制配置：如何创建自定义的配置信息？》中，我们介绍了自定义配置信息的实现方式。而在 Spring Boot 应用程序中，Service 层通常依赖于配置文件，所以我们也需要对配置信息进行测试。</p>
<p>配置信息的测试方案分为两种，第一种依赖于物理配置文件，第二种则是在测试时动态注入配置信息。</p>
<p>第一种测试方案比较简单，在 src/test/resources 目录下添加配置文件时，Spring Boot 能读取这些配置文件中的配置项并应用于测试案例中。在介绍具体的实现过程之前，我们有必要先来了解一下 Environment 接口，该接口定义如下：</p>
<pre><code>public interface Environment extends PropertyResolver {

    String[] getActiveProfiles();

    String[] getDefaultProfiles();

    boolean acceptsProfiles(String... profiles);

}
</code></pre>
<p>在上述代码中我们可以看到，Environment 接口的主要作用是处理 Profile，而它的父接口 PropertyResolver 定义如下代码所示：</p>
<pre><code>public interface PropertyResolver {

    boolean containsProperty(String key);

    String getProperty(String key);

    String getProperty(String key, String defaultValue);

    &lt;T&gt; T getProperty(String key, Class&lt;T&gt; targetType);

    &lt;T&gt; T getProperty(String key, Class&lt;T&gt; targetType, T defaultValue);

    String getRequiredProperty(String key) throws IllegalStateException;

    &lt;T&gt; T getRequiredProperty(String key, Class&lt;T&gt; targetType) throws IllegalStateException;

    String resolvePlaceholders(String text);

    String resolveRequiredPlaceholders(String text) throws IllegalArgumentException;

}
</code></pre>
<p>显然，PropertyResolver 的作用是根据各种配置项的 Key 获取配置属性值。</p>
<p>现在，假设 src/test/resources 目录中的 application.properties 存在如下配置项：</p>
<pre><code>springcss.order.point = 10
</code></pre>
<p>那么，我们就可以设计如下所示的测试用例了。</p>
<pre><code>@RunWith(SpringRunner.class)

@SpringBootTest

public class EnvironmentTests{

 

    @Autowired

    public Environment environment;

 

    @Test

    public void testEnvValue(){

        Assert.assertEquals(10, Integer.parseInt(environment.getProperty(&quot;springcss.order.point&quot;))); 

    }

}
</code></pre>
<p>这里我们注入了一个 Environment 接口，并调用了它的 getProperty 方法来获取测试环境中的配置信息。</p>
<p>除了在配置文件中设置属性，我们也可以使用 @SpringBootTest 注解指定用于测试的属性值，示例代码如下：</p>
<pre><code>@RunWith(SpringRunner.class)

@SpringBootTest(properties = {&quot; springcss.order.point = 10&quot;})

public class EnvironmentTests{

 

    @Autowired

    public Environment environment;

 

    @Test

    public void testEnvValue(){

        Assert.assertEquals(10, Integer.parseInt(environment.getProperty(&quot;springcss.order.point&quot;))); 

    }

}
</code></pre>
<h3>使用 Mock 测试 Service 层</h3>
<p>正如这一讲开篇时提到，Service 层依赖于数据访问层。因此，对 Service 层进行测试时，我们还需要引入新的技术体系，也就是应用非常广泛的 Mock 机制。</p>
<p>接下来，我们先看一下 Mock 机制的基本概念。</p>
<h4>Mock 机制</h4>
<p>Mock 的意思是模拟，它可以用来对系统、组件或类进行隔离。</p>
<p>在测试过程中，我们通常关注测试对象本身的功能和行为，而对测试对象涉及的一些依赖，仅仅关注它们与测试对象之间的交互（比如是否调用、何时调用、调用的参数、调用的次数和顺序，以及返回的结果或发生的异常等），并不关注这些被依赖对象如何执行这次调用的具体细节。因此，Mock 机制就是使用 Mock 对象替代真实的依赖对象，并模拟真实场景来开展测试工作。</p>
<p>使用 Mock 对象完成依赖关系测试的示意图如下所示：</p>
<p><img src="assets/CioPOWAdHoyAZcf6AACLingamrY696.png" alt="图片1.png" /></p>
<p>Mock 对象与依赖关系测试示意图</p>
<p>从图中可以看出，在形式上，Mock 是在测试代码中直接 Mock 类和定义 Mock 方法的行为，通常测试代码和 Mock 代码放一起。因此，测试代码的逻辑从测试用例的代码上能很容易地体现出来。</p>
<p>下面我们一起看一下如何使用 Mock 测试 Service 层。</p>
<h4>使用 Mock</h4>
<p>23 讲中我们介绍了 @SpringBootTest 注解中的 SpringBootTest.WebEnvironment.MOCK 选项，该选项用于加载 WebApplicationContext 并提供一个 Mock 的 Servlet 环境，内置的 Servlet 容器并没有真实启动。接下来，我们针对 Service 层演示一下这种测试方式。</p>
<p>首先，我们来看一种简单场景，在 customer-service 中存在如下 CustomerTicketService 类：</p>
<pre><code>@Service

public class CustomerTicketService {

 

    @Autowired

    private CustomerTicketRepository customerTicketRepository;

 

    public CustomerTicket getCustomerTicketById(Long id) {

        return customerTicketRepository.getOne(id);

    }

    …

}
</code></pre>
<p>这里我们可以看到，以上方法只是简单地通过 CustomerTicketRepository 完成了数据查询操作。</p>
<p>显然，对以上 CustomerTicketService 进行集成测试时，还需要我们提供一个 CustomerTicketRepository 依赖。</p>
<p>下面，我们通过以下代码演示一下如何使用 Mock 机制完成对 CustomerTicketRepository 的隔离。</p>
<pre><code>@RunWith(SpringRunner.class)

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.MOCK)

public class CustomerServiceTests {

 

    @MockBean

    private CustomerTicketRepository customerTicketRepository;

 

    @Test

    public void testGetCustomerTicketById() throws Exception {

        Long id = 1L;

       Mockito.when(customerTicketRepository.getOne(id)).thenReturn(new CustomerTicket(1L, 1L, &quot;Order00001&quot;, &quot;DemoCustomerTicket1&quot;, new Date()));

        CustomerTicket actual = customerTicketService.getCustomerTicketById(id);

 

        assertThat(actual).isNotNull();

        assertThat(actual.getOrderNumber()).isEqualTo(&quot;Order00001&quot;);

    }

}
</code></pre>
<p>首先，我们通过 @MockBean 注解注入了 CustomerTicketRepository；然后，基于第三方 Mock 框架 Mockito 提供的 when/thenReturn 机制完成了对 CustomerTicketRepository 中 getCustomerTicketById() 方法的 Mock。</p>
<p>当然，如果你希望在测试用例中直接注入真实的CustomerTicketRepository，这时就可以使用@SpringBootTest 注解中的 SpringBootTest.WebEnvironment.RANDOM_PORT 选项，示例代码如下：</p>
<pre><code>@RunWith(SpringRunner.class)

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)

public class CustomerServiceTests {

 

    @Autowired

    private CustomerTicketRepository customerTicketRepository;

 

    @Test

    public void testGetCustomerTicketById() throws Exception {

        Long id = 1L;

        CustomerTicket actual = customerTicketService.getCustomerTicketById(id);

 

        assertThat(actual).isNotNull();

        assertThat(actual.getOrderNumber()).isEqualTo(&quot;Order00001&quot;);

    }

}
</code></pre>
<p>运行上述代码后就会以一个随机的端口启动整个 Spring Boot 工程，并从数据库中真实获取目标数据进行验证。</p>
<p>以上集成测试的示例中只包含了对 Repository 层的依赖，而有时候一个 Service 中可能同时包含 Repository 和其他 Service 类或组件，下面回到如下所示的 CustomerTicketService 类：</p>
<pre><code>@Service

public class CustomerTicketService {

 

    @Autowired

    private OrderClient orderClient;

 

    private OrderMapper getRemoteOrderByOrderNumber(String orderNumber) {

 

        return orderClient.getOrderByOrderNumber(orderNumber);

    }

    …

}
</code></pre>
<p>这里我们可以看到，在该代码中，除了依赖 CustomerTicketRepository 之外，还同时依赖了 OrderClient。</p>
<p><strong>请注意：以上代码中的 OrderClient 是在 customer-service 中通过 RestTemplate 访问 order-service 的远程实现类，其代码如下所示：</strong></p>
<pre><code>@Component

public class OrderClient {

 

    @Autowired

    RestTemplate restTemplate;

 

    public OrderMapper getOrderByOrderNumber(String orderNumber) {

 

        ResponseEntity&lt;OrderMapper&gt; restExchange = restTemplate.exchange(

                &quot;http://localhost:8083/orders/{orderNumber}&quot;, HttpMethod.GET, null,

                OrderMapper.class, orderNumber);

 

         OrderMapper result = restExchange.getBody();

 

        return result;

    }

}
</code></pre>
<p>CustomerTicketService 类实际上并不关注 OrderClient 中如何实现远程访问的具体过程。因为对于集成测试而言，它只关注方法调用返回的结果，所以我们将同样采用 Mock 机制完成对 OrderClient 的隔离。</p>
<p>对 CustomerTicketService 这部分功能的测试用例代码如下所示，可以看到，我们采用的是同样的测试方式。</p>
<pre><code>@Test

public void testGenerateCustomerTicket() throws Exception {

        Long accountId = 100L;

        String orderNumber = &quot;Order00001&quot;;

        Mockito.when(this.orderClient.getOrderByOrderNumber(&quot;Order00001&quot;))

            .thenReturn(new OrderMapper(1L, orderNumber, &quot;deliveryAddress&quot;));

        Mockito.when(this.localAccountRepository.getOne(accountId))

            .thenReturn(new LocalAccount(100L, &quot;accountCode&quot;, &quot;accountName&quot;));

 

        CustomerTicket actual = customerTicketService.generateCustomerTicket(accountId, orderNumber);

 

        assertThat(actual.getOrderNumber()).isEqualTo(orderNumber);

}
</code></pre>
<p>这里提供的测试用例演示了 Service 层中进行集成测试的各种手段，它们已经能够满足一般场景的需要。</p>
<h3>测试 Controller 层</h3>
<p>对 Controller 层进行测试之前，我们先来提供一个典型的 Controller 类，它来自 customer-service，如下代码所示：</p>
<pre><code>@RestController

@RequestMapping(value=&quot;customers&quot;)

public class CustomerController {

    @Autowired

    private CustomerTicketService customerTicketService; 

    @PostMapping(value = &quot;/{accountId}/{orderNumber}&quot;)

    public CustomerTicket generateCustomerTicket( @PathVariable(&quot;accountId&quot;) Long accountId,

            @PathVariable(&quot;orderNumber&quot;) String orderNumber) {

        CustomerTicket customerTicket = customerTicketService.generateCustomerTicket(accountId, orderNumber);

        return customerTicket;

    }

}
</code></pre>
<p>关于上述 Controller 类的测试方法，相对来说比较丰富，比如有 TestRestTemplate、@WebMvcTest 注解和 MockMvc 这三种，下面我们逐一进行讲解。</p>
<h4>使用 TestRestTemplate</h4>
<p>Spring Boot 提供的 TestRestTemplate 与 RestTemplate 非常类似，只不过它专门用在测试环境中。</p>
<p>如果我们想在测试环境中使用 @SpringBootTest，则可以直接使用 TestRestTemplate 来测试远程访问过程，示例代码如下：</p>
<pre><code>@RunWith(SpringRunner.class)

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)

public class CustomerController2Tests {

 

    @Autowired

    private TestRestTemplate testRestTemplate;

 

    @MockBean

    private CustomerTicketService customerTicketService;

 

    @Test

    public void testGenerateCustomerTicket() throws Exception {

        Long accountId = 100L;

        String orderNumber = &quot;Order00001&quot;;

        given(this.customerTicketService.generateCustomerTicket(accountId, orderNumber))

                .willReturn(new CustomerTicket(1L, accountId, orderNumber, &quot;DemoCustomerTicket1&quot;, new Date()));

 

        CustomerTicket actual = testRestTemplate.postForObject(&quot;/customers/&quot; + accountId+ &quot;/&quot; + orderNumber, null, CustomerTicket.class);

        assertThat(actual.getOrderNumber()).isEqualTo(orderNumber);

    }

}
</code></pre>
<p>上述测试代码中，首先，我们注意到 @SpringBootTest 注解通过使用 SpringBootTest.WebEnvironment.RANDOM_PORT 指定了随机端口的 Web 运行环境。然后，我们基于 TestRestTemplate 发起了 HTTP 请求并验证了结果。</p>
<p><strong>特别说明：这里使用 TestRestTemplate 发起请求的方式与 RestTemplate 完全一致，你可以对《服务调用：如何使用 RestTemplate 消费 RESTful 服务？》的内容进行回顾。</strong></p>
<h4>使用 @WebMvcTest 注解</h4>
<p>接下来测试方法中，我们将引入一个新的注解 @WebMvcTest，该注解将初始化测试 Controller 所必需的 Spring MVC 基础设施，CustomerController 类的测试用例如下所示：</p>
<pre><code>@RunWith(SpringRunner.class)

@WebMvcTest(CustomerController.class)

public class CustomerControllerTestsWithMockMvc {

 

    @Autowired

    private MockMvc mvc;

 

    @MockBean

    private CustomerTicketService customerTicketService;

 

    @Test

    public void testGenerateCustomerTicket() throws Exception {

        Long accountId = 100L;

        String orderNumber = &quot;Order00001&quot;;

        given(this.customerTicketService.generateCustomerTicket(accountId, orderNumber))

                .willReturn(new CustomerTicket(1L, 100L, &quot;Order00001&quot;, &quot;DemoCustomerTicket1&quot;, new Date()));

 

        this.mvc.perform(post(&quot;/customers/&quot; + accountId+ &quot;/&quot; + orderNumber).accept(MediaType.APPLICATION_JSON)).andExpect(status().isOk());

    }

}
</code></pre>
<p>以上代码的关键是 MockMvc 工具类，所以接下来我们有必要对它进一步展开说明。</p>
<p>MockMvc 类提供的基础方法分为以下 6 种，下面一一对应来看下。</p>
<ul>
<li><strong>Perform</strong>：执行一个 RequestBuilder 请求，会自动执行 SpringMVC 流程并映射到相应的 Controller 进行处理。</li>
<li><strong>get/post/put/delete</strong>：声明发送一个 HTTP 请求的方式，根据 URI 模板和 URI 变量值得到一个 HTTP 请求，支持 GET、POST、PUT、DELETE 等 HTTP 方法。</li>
<li><strong>param</strong>：添加请求参数，发送 JSON 数据时将不能使用这种方式，而应该采用 @ResponseBody 注解。</li>
<li><strong>andExpect</strong>：添加 ResultMatcher 验证规则，通过对返回的数据进行判断来验证 Controller 执行结果是否正确。</li>
<li><strong>andDo</strong>：添加 ResultHandler 结果处理器，比如调试时打印结果到控制台。</li>
<li><strong>andReturn</strong>：最后返回相应的 MvcResult，然后执行自定义验证或做异步处理。</li>
</ul>
<p>执行该测试用例后，从输出的控制台日志中我们不难发现，整个流程相当于启动了 CustomerController 并执行远程访问，而 CustomerController 中使用的 CustomerTicketService 则做了 Mock。</p>
<p>显然，测试 CustomerController 的目的在于验证其返回数据的格式和内容。在上述代码中，我们先定义了 CustomerController 将会返回的 JSON 结果，然后通过 perform、accept 和 andExpect 方法模拟了 HTTP 请求的整个过程，最终验证了结果的正确性。</p>
<h4>使用 @AutoConfigureMockMvc 注解</h4>
<p><strong>请注意 @SpringBootTest 注解不能和 @WebMvcTest 注解同时使用。</strong></p>
<p>在使用 @SpringBootTest 注解的场景下，如果我们想使用 MockMvc 对象，那么可以引入 @AutoConfigureMockMvc 注解。</p>
<p>通过将 @SpringBootTest 注解与 @AutoConfigureMockMvc 注解相结合，@AutoConfigureMockMvc 注解将通过 @SpringBootTest 加载的 Spring 上下文环境中自动配置 MockMvc 这个类。</p>
<p>使用 @AutoConfigureMockMvc 注解的测试代码如下所示：</p>
<pre><code>@RunWith(SpringRunner.class)

@SpringBootTest

@AutoConfigureMockMvc

public class CustomerControllerTestsWithAutoConfigureMockMvc {

 

    @Autowired

    private MockMvc mvc;

 

    @MockBean

    private CustomerTicketService customerTicketService;

 

    @Test

    public void testGenerateCustomerTicket() throws Exception {

        Long accountId = 100L;

        String orderNumber = &quot;Order00001&quot;;

        given(this.customerTicketService.generateCustomerTicket(accountId, orderNumber))

                .willReturn(new CustomerTicket(1L, 100L, &quot;Order00001&quot;, &quot;DemoCustomerTicket1&quot;, new Date()));

 

        this.mvc.perform(post(&quot;/customers/&quot; + accountId+ &quot;/&quot; + orderNumber).accept(MediaType.APPLICATION_JSON)).andExpect(status().isOk());

    }

}
</code></pre>
<p>在上述代码中，我们使用了 MockMvc 工具类完成了对 HTTP 请求的模拟，并基于返回状态验证了 Controller 层组件的正确性。</p>
<h3>Spring Boot 中的测试注解总结</h3>
<p>通过前面内容的学习，相信你已经感受到了各种测试注解在测试 Spring Boot 应用程序的过程中所发挥的核心作用。</p>
<p>如下所示表格，我们罗列了一些经常使用的测试注解及其描述。</p>
<p><img src="assets/Cgp9HWAdHqiAdUEbAAG7s2vEMgM538.png" alt="图片8.png" /></p>
<h3>小结与预告</h3>
<p>对于一个 Web 应用程序而言，Service 层和 Web 层组件的测试是核心关注点。这一讲我们通过 Mock 机制实现了 Service 层的测试，并引入了三种不同的方法对 Controller 层组件完成验证。</p>
<p>这里给你留一道思考题：在使用 Spring Boot 测试 Web 应用程序时，你知道常见的测试注解有哪些？欢迎在留言区进行互动、交流。</p>
<p>讲完测试组件之后，我们将进入本专栏的最后一讲。在结束语中，我们将对 Spring Boot 进行总结，并对它的后续发展进行展望。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="23&#32;&#32;数据测试：如何使用&#32;Spring&#32;测试数据访问层组件？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="结束语&#32;&#32;以终为始：Spring&#32;Boot&#32;总结和展望.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434d6bdaec70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
