<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>23  数据测试：如何使用 Spring 测试数据访问层组件？.md</title>
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

                    <a class="current-tab" href="23&#32;&#32;数据测试：如何使用&#32;Spring&#32;测试数据访问层组件？.md">23  数据测试：如何使用 Spring 测试数据访问层组件？.md</a>
                    

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
                        <div><h1>23  数据测试：如何使用 Spring 测试数据访问层组件？</h1>
<p>作为整个课程最后一部分内容，从这一讲开始，我们将讨论 Spring 提供的测试解决方案。对于 Web 应用程序而言，测试是一个难点，也是经常被忽略的一套技术体系。一个应用程序中涉及数据层、服务层、Web 层，以及各种外部服务之间的交互关系时，我们除了对各层组件的单元测试之外，还需要充分引入集成测试保证服务的正确性和稳定性。</p>
<h3>Spring Boot 中的测试解决方案</h3>
<p>和 Spring Boot 1.x 版本一样，Spring Boot 2.x 也提供了一个用于测试的 spring-boot-starter-test 组件。</p>
<p>在 Spring Boot 中，集成该组件的方法是在 pom 文件中添加如下所示依赖：</p>
<pre><code>&lt;dependency&gt;

    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;

    &lt;artifactId&gt;spring-boot-starter-test&lt;/artifactId&gt;

    &lt;scope&gt;test&lt;/scope&gt;

&lt;/dependency&gt;

        

&lt;dependency&gt;

    &lt;groupId&gt;org.junit.platform&lt;/groupId&gt;

    &lt;artifactId&gt;junit-platform-launcher&lt;/artifactId&gt;

    &lt;scope&gt;test&lt;/scope&gt;

&lt;/dependency&gt;
</code></pre>
<p>其中，最后一个依赖用于导入与 JUnit 相关的功能组件。</p>
<p>然后，通过 Maven 查看 spring-boot-starter-test 组件的依赖关系，我们可以得到如下所示的组件依赖图：</p>
<p><img src="assets/CgpVE2AYyZ6ADMDGAAVPdtkysNI580.png" alt="Drawing 1.png" /></p>
<p>spring-boot-starter-test 组件的依赖关系图</p>
<p>在《案例驱动：如何剖析一个 Spring Web 应用程序？》中我们提到，Spring Boot 使得编码、配置、部署和监控工作更简单。事实上，Spring Boot 也能让测试工作更加简单。</p>
<p>从上图中可以看到，在代码工程的构建路径中，我们引入了一系列组件初始化测试环境。比如 JUnit、JSON Path、AssertJ、Mockito、Hamcrest 等，这里我们有必要对这些组件进行展开说明。</p>
<ul>
<li><strong>JUnit</strong>：JUnit 是一款非常流行的基于 Java 语言的单元测试框架，在我们的课程中主要使用该框架作为基础的测试框架。</li>
<li><strong>JSON Path</strong>：类似于 XPath 在 XML 文档中的定位，JSON Path 表达式通常用来检索路径或设置 JSON 文件中的数据。</li>
<li><strong>AssertJ</strong>：AssertJ 是一款强大的流式断言工具，它需要遵守 3A 核心原则，即 Arrange（初始化测试对象或准备测试数据）——&gt; Actor（调用被测方法）——&gt;Assert（执行断言）。</li>
<li><strong>Mockito</strong>：Mockito 是 Java 世界中一款流行的 Mock 测试框架，它主要使用简洁的 API 实现模拟操作。在实施集成测试时，我们将大量使用到这个框架。</li>
<li><strong>Hamcrest</strong>：Hamcrest 提供了一套匹配器（Matcher），其中每个匹配器的设计用于执行特定的比较操作。</li>
<li><strong>JSONassert</strong>：JSONassert 是一款专门针对 JSON 提供的断言框架。</li>
<li><strong>Spring Test &amp; Spring Boot Test</strong>：为 Spring 和 Spring Boot 框架提供的测试工具。</li>
</ul>
<p>以上组件的依赖关系都是自动导入，我们无须做任何变动。而对于某些特定场景而言，就需要我们手工导入一些组件以满足测试需求，例如引入专用针对测试场景的嵌入式关系型数据库 H2。</p>
<h3>测试 Spring Boot 应用程序</h3>
<p>接下来，我们将初始化 Spring Boot 应用程序的测试环境，并介绍如何在单个服务内部完成单元测试的方法和技巧。</p>
<p>导入 spring-boot-starter-test 依赖后，我们就可以使用它提供的各项功能应对复杂的测试场景了。</p>
<h4>初始化测试环境</h4>
<p>对于 Spring Boot 应用程序而言，我们知道其 Bootstrap 类中的 main() 入口将通过 SpringApplication.run() 方法启动 Spring 容器，如下所示的 CustomerApplication 类就是一个典型的 Spring Boot 启动类 ：</p>
<pre><code>@SpringBootApplication

public class CustomerApplication {

    

        public static void main(String[] args) {

            SpringApplication.run(CustomerApplication.class, args);

        }

}
</code></pre>
<p>针对上述 Bootstrap 类，我们可以通过编写测试用例的方式，验证 Spring 容器能否正常启动。</p>
<p>为了添加测试用例，我们有必要梳理一下代码的组织结构，梳理完后就呈现了如下图所示的customer-service 工程中代码的基本目录结构。</p>
<p><img src="assets/CgpVE2AYycmAXHkdAAdjApgDr7s414.png" alt="Drawing 3.png" /></p>
<p>customer-service 工程代码目录结构</p>
<p>基于 Maven 的默认风格，我们将在 src/test/java 和 src/test/resources 包下添加各种测试用例代码和配置文件，正如上图所示。</p>
<p>打开上图中的 ApplicationContextTests.java 文件，我们可以得到如下所示的测试用例代码：</p>
<pre><code>import org.junit.Assert;

import org.junit.Test;

import org.junit.runner.RunWith;

import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.boot.test.context.SpringBootTest;

import org.springframework.context.ApplicationContext;

import org.springframework.test.context.junit4.SpringRunner;

 

@SpringBootTest

@RunWith(SpringRunner.class)

public class ApplicationContextTests {

 

    @Autowired

    private ApplicationContext applicationContext;

 

    @Test

    public void testContextLoads() throws Throwable {

        Assert.assertNotNull(this.applicationContext);

    }

}
</code></pre>
<p>该代码中的 testContextLoaded() 就是一个有效的测试用例，这里我们可以看到该用例对 Spring 中的 ApplicationContext 作了简单非空验证。</p>
<p>执行该测试用例后，从输出的控制台信息中，我们可以看到 Spring Boot 应用程序被正常启动，同时测试用例本身也会给出执行成功的提示。</p>
<p>上述测试用例虽然简单，但是已经包含了测试 Spring Boot 应用程序的基本代码框架。其中，最重要的是 ApplicationContextTests 类上的 @SpringBootTest 和 @RunWith 注解，对于 Spring Boot 应用程序而言，这两个注解构成了一套完成的测试方案。</p>
<p>接下来我们对这两个注解进行详细展开。</p>
<h4>@SpringBootTest 注解</h4>
<p>因为 SpringBoot 程序的入口是 Bootstrap 类，所以 SpringBoot 专门提供了一个 @SpringBootTest 注解测试 Bootstrap 类。同时 @SpringBootTest 注解也可以引用 Bootstrap 类的配置，因为所有配置都会通过 Bootstrap 类去加载。</p>
<p>在上面的例子中，我们是通过直接使用 @SpringBootTest 注解提供的默认功能对作为 Bootstrap 类的 Application 类进行测试。而更常见的做法是在 @SpringBootTest 注解中指定该 Bootstrap 类，并设置测试的 Web 环境，如下代码所示。</p>
<pre><code>@SpringBootTest(classes = CustomerApplication.class, 

	webEnvironment = SpringBootTest.WebEnvironment.MOCK)
</code></pre>
<p>在以上代码中，@SpringBootTest 注解中的 webEnvironment 可以有四个选项，分别是 MOCK、RANDOM_PORT、DEFINED_PORT 和 NONE。</p>
<ul>
<li><strong>MOCK</strong>：加载 WebApplicationContext 并提供一个 Mock 的 Servlet 环境，此时内置的 Servlet 容器并没有正式启动。</li>
<li><strong>RANDOM_PORT</strong>：加载 EmbeddedWebApplicationContext 并提供一个真实的 Servlet 环境，然后使用一个随机端口启动内置容器。</li>
<li><strong>DEFINED_PORT</strong>：这个配置也是通过加载 EmbeddedWebApplicationContext 提供一个真实的 Servlet 环境，但使用的是默认端口，如果没有配置端口就使用 8080。</li>
<li><strong>NONE</strong>：加载 ApplicationContext 但并不提供任何真实的 Servlet 环境。</li>
</ul>
<p>在 Spring Boot 中，@SpringBootTest 注解主要用于测试基于自动配置的 ApplicationContext，它允许我们设置测试上下文中的 Servlet 环境。</p>
<p>在多数场景下，一个真实的 Servlet 环境对于测试而言过于重量级，通过 MOCK 环境则可以缓解这种环境约束所带来的成本和挑战。在 22 讲《服务测试：如何使用Spring测试Web服务层组件？》中，我们将结合 WebEnvironment.MOCK 选项对服务层中的具体功能进行集成测试。</p>
<h4>@RunWith 注解与 SpringRunner</h4>
<p>在上面的示例中，我们还看到一个由 JUnit 框架提供的 @RunWith 注解，它用于设置测试运行器。例如，我们可以通过 @RunWith(SpringJUnit4ClassRunner.class) 让测试运行于 Spring 测试环境。</p>
<p>虽然这我们指定的是 SpringRunner.class，实际上，SpringRunner 就是 SpringJUnit4ClassRunner 的简化，它允许 JUnit 和 Spring TestContext 整合运行，而 Spring TestContext 则提供了用于测试 Spring 应用程序的各项通用的支持功能。</p>
<p>在后续的测试用例中，我们将大量使用 SpringRunner。</p>
<h4>执行测试用例</h4>
<p>在这一讲中，我们还将通过代码示例回顾如何使用 JUnit 框架执行单元测试的过程和实践，同时提供验证异常和验证正确性的测试方法。</p>
<p>单元测试的应用场景是一个独立的类，如下所示的 CustomerTicket 类就是一个非常典型的独立类：</p>
<hr />
<pre><code>public class CustomerTicket {

    private Long id;

    private Long accountId;    

    private String orderNumber;

    private String description;

    private Date createTime;

    

        

    public CustomerTicket(Long accountId, String orderNumber) {

        super();

        

        Assert.notNull(accountId, &quot;Account Id must not be null&quot;);

        Assert.notNull(orderNumber, &quot;Order Number must not be null&quot;);

        Assert.isTrue(orderNumber.length() == 10, &quot;Order Number must be exactly 10 characters&quot;);

 

        this.accountId = accountId;

        this.orderNumber = orderNumber;

    }

       …

}
</code></pre>
<p>从中我们可以看到，该类对客服工单做了封装，并在其构造函数中添加了校验机制。</p>
<p>下面我们先来看看如何对正常场景进行测试。</p>
<p>例如 CustomerTicket 中orderNumber 的长度问题，我们可以使用如下测试用例，通过在构造函数中传入字符串来验证规则的正确性：</p>
<pre><code>@RunWith(SpringRunner.class)

public class CustomerTicketTests {

 

    private static final String ORDER_NUMBER = &quot;Order00001&quot;;

 

    @Test

    public void testOrderNumberIsExactly10Chars() throws Exception {

 

        CustomerTicket customerTicket = new CustomerTicket(100L, ORDER_NUMBER);

 

                assertThat(customerTicket.getOrderNumber().toString()).isEqualTo(ORDER_NUMBER);

    }

}
</code></pre>
<p>执行这个单元测试后，我们就可以看到执行的过程及结果。</p>
<p>而这些单元测试用例只是演示了最基本的测试方式，后续的各种测试机制我们将在此基础上进行扩展和演化。</p>
<h3>使用 @DataJpaTest 注解测试数据访问组件</h3>
<p>数据需要持久化，接下来我们将从数据持久化的角度出发，讨论如何对 Repository 层进行测试的方法。</p>
<p>首先，我们讨论一下使用关系型数据库的场景，并引入针对 JPA 数据访问技术的 @DataJpaTest 注解。</p>
<p>@DataJpaTest 注解会自动注入各种 Repository 类，并初始化一个内存数据库和及访问该数据库的数据源。在测试场景下，一般我们可以使用 H2 作为内存数据库，并通过 MySQL 实现数据持久化，因此我们需要引入以下所示的 Maven 依赖：</p>
<pre><code>&lt;dependency&gt;

       &lt;groupId&gt;com.h2database&lt;/groupId&gt;

       &lt;artifactId&gt;h2&lt;/artifactId&gt;

&lt;/dependency&gt;

 

&lt;dependency&gt;

       &lt;groupId&gt;mysql&lt;/groupId&gt;

       &lt;artifactId&gt;mysql-connector-java&lt;/artifactId&gt;

       &lt;scope&gt;runtime&lt;/scope&gt;

&lt;/dependency&gt;
</code></pre>
<p>另一方面，我们需要准备数据库 DDL 用于初始化数据库表，并提供 DML 脚本完成数据初始化。其中，schema-mysql.sql 和 data-h2.sql 脚本分别充当了 DDL 和 DML 的作用。</p>
<p>在 customer-service 的 schema-mysql.sql 中包含了 CUSTOMER 表的创建语句，如下代码所示：</p>
<pre><code>DROP TABLE IF EXISTS `customerticket`;

create table `customerticket` (

	   `id` bigint(20) NOT NULL AUTO_INCREMENT,

	   `account_id` bigint(20) not null,

	   `order_number` varchar(50) not null,

	   `description` varchar(100) not null,

	    `create_time` timestamp not null DEFAULT CURRENT_TIMESTAMP,

	   PRIMARY KEY (`id`)

);
</code></pre>
<p>而在 data-h2.sql 中，我们插入了一条测试需要使用的数据，具体的初始化数据过程如下代码所示：</p>
<pre><code>INSERT INTO customerticket (`account_id`, `order_number`,`description`) values (1, 'Order00001', ' DemoCustomerTicket1');
</code></pre>
<p>接下来是提供具体的 Repository 接口，我们先通过如下所示代码回顾一下 CustomerRepository 接口的定义。</p>
<pre><code>public interface CustomerTicketRepository extends JpaRepository&lt;CustomerTicket, Long&gt; {

    

    List&lt;CustomerTicket&gt; getCustomerTicketByOrderNumber(String orderNumber);

}
</code></pre>
<p>这里存在一个方法名衍生查询 getCustomerTicketByOrderNumber，它会根据 OrderNumber 获取 CustomerTicket。</p>
<p>基于上述 CustomerRepository，我们可以编写如下所示的测试用例：</p>
<pre><code>@RunWith(SpringRunner.class)

@DataJpaTest

public class CustomerRepositoryTest {

    

    @Autowired

    private TestEntityManager entityManager;

 

    @Autowired

    private CustomerTicketRepository customerTicketRepository;

 

    @Test

    public void testFindCustomerTicketById() throws Exception {             

        this.entityManager.persist(new CustomerTicket(1L, &quot;Order00001&quot;, &quot;DemoCustomerTicket1&quot;, new Date()));

        

        CustomerTicket customerTicket = this.customerTicketRepository.getOne(1L);

        assertThat(customerTicket).isNotNull();

        assertThat(customerTicket.getId()).isEqualTo(1L);

    }

        

    @Test

    public void testFindCustomerTicketByOrderNumber() throws Exception {    

        String orderNumber = &quot;Order00001&quot;;

        

        this.entityManager.persist(new CustomerTicket(1L, orderNumber, &quot;DemoCustomerTicket1&quot;, new Date()));

        this.entityManager.persist(new CustomerTicket(2L, orderNumber, &quot;DemoCustomerTicket2&quot;, new Date()));

        

        List&lt;CustomerTicket&gt; customerTickets = this.customerTicketRepository.getCustomerTicketByOrderNumber(orderNumber);

        assertThat(customerTickets).size().isEqualTo(2);

        CustomerTicket actual = customerTickets.get(0);

        assertThat(actual.getOrderNumber()).isEqualTo(orderNumber);

    }

 

    @Test

    public void testFindCustomerTicketByNonExistedOrderNumber() throws Exception {              

        this.entityManager.persist(new CustomerTicket(1L, &quot;Order00001&quot;, &quot;DemoCustomerTicket1&quot;, new Date()));

        this.entityManager.persist(new CustomerTicket(2L, &quot;Order00002&quot;, &quot;DemoCustomerTicket2&quot;, new Date()));

        

        List&lt;CustomerTicket&gt; customerTickets = this.customerTicketRepository.getCustomerTicketByOrderNumber(&quot;Order00003&quot;);

        assertThat(customerTickets).size().isEqualTo(0);

    }

}
</code></pre>
<p>这里可以看到，我们使用了 @DataJpaTest 实现 CustomerRepository 的注入。同时，我们还注意到另一个核心测试组件 TestEntityManager，它的效果相当于不使用真正的 CustomerRepository 完成数据的持久化，从而提供了一种数据与环境之间的隔离机制。</p>
<p>执行这些测试用例后，我们需要关注它们的控制台日志输入，其中核心日志如下所示（为了显示做了简化处理）：</p>
<pre><code>Hibernate: drop table customer_ticket if exists

Hibernate: drop sequence if exists hibernate_sequence

Hibernate: create sequence hibernate_sequence start with 1 increment by 1

Hibernate: create table customer_ticket (id bigint not null, account_id bigint, create_time timestamp, description varchar(255), order_number varchar(255), primary key (id))

Hibernate: create table localaccount (id bigint not null, account_code varchar(255), account_name varchar(255), primary key (id))

…

Hibernate: call next value for hibernate_sequence

Hibernate: call next value for hibernate_sequence

Hibernate: insert into customer_ticket (account_id, create_time, description, order_number, id) values (?, ?, ?, ?, ?)

Hibernate: insert into customer_ticket (account_id, create_time, description, order_number, id) values (?, ?, ?, ?, ?)

Hibernate: select customerti0_.id as id1_0_, customerti0_.account_id as account_2_0_, customerti0_.create_time as create_t3_0_, customerti0_.description as descript4_0_, customerti0_.order_number as order_nu5_0_ from customer_ticket customerti0_ where customerti0_.order_number=?

…

Hibernate: drop table customer_ticket if exists

Hibernate: drop sequence if exists hibernate_sequence
</code></pre>
<p>从以上日志中，我们不难看出执行各种 SQL 语句的效果，此时你也可以修改这些测试用例，并观察执行结果。</p>
<h3>小结与预告</h3>
<p>测试是一套独立的技术体系，需要开发人员充分重视且付诸实践，这点对于 Web 应用程序测试而言更是如此。这一讲我们基于 Spring Boot 给出了完整的测试方法和核心注解，并针对关系型数据库给出了数据访问组件的测试过程。</p>
<p>这里给你留一道思考题：在使用 Spring Boot 执行测试用例时，如何基于内存数据库完成数据访问过程的测试？欢迎你在留言区与我交流、互动哦~</p>
<p>介绍完数据库访问测试之后，24 讲我们将讨论如何对 Web 服务层组件进行测试。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="22&#32;&#32;运行管理：如何使用&#32;Admin&#32;Server&#32;管理&#32;Spring&#32;应用程序？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="24&#32;&#32;服务测试：如何使用&#32;Spring&#32;测试&#32;Web&#32;服务层组件？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434d64c8bb70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
