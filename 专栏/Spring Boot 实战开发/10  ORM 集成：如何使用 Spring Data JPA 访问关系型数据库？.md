<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>10  ORM 集成：如何使用 Spring Data JPA 访问关系型数据库？.md</title>
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

                    <a class="current-tab" href="10&#32;&#32;ORM&#32;集成：如何使用&#32;Spring&#32;Data&#32;JPA&#32;访问关系型数据库？.md">10  ORM 集成：如何使用 Spring Data JPA 访问关系型数据库？.md</a>
                    

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
                        <div><h1>10  ORM 集成：如何使用 Spring Data JPA 访问关系型数据库？</h1>
<p>在前面的课程中，我们详细介绍了如何使用 Spring 所提供的 JdbcTemplate 模板工具类实现数据访问的实现方法。相较 JDBC 所提供的原生 API，JdbcTemplate 做了一层封装，大大简化了数据的操作过程。而在 09 讲中，我们又进一步引入了 Spring Data 框架，可以说 Spring Data 框架是基于 JdbcTemplate 上另一层更高级的封装。</p>
<p>今天，我们将基于 Spring Data 中的 Spring Data JPA 组件介绍如何集成 ORM 框架实现关系型数据库访问。</p>
<h3>引入 Spring Data JPA</h3>
<p>如果你想在应用程序中使用 Spring Data JPA，首先需要在 pom 文件中引入 spring-boot-starter-data-jpa 依赖，如下代码所示：</p>
<pre><code>&lt;dependency&gt;

     &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;

     &lt;artifactId&gt;spring-boot-starter-data-jpa&lt;/artifactId&gt;

&lt;/dependency&gt;
</code></pre>
<p>在介绍这一组件的使用方法之前，我们有必要对 JPA 规范进行一定的了解。</p>
<p>JPA 全称是 JPA Persistence API，即 Java 持久化 API，它是一个 Java 应用程序接口规范，用于充当面向对象的领域模型和关系数据库系统之间的桥梁，属于一种 ORM（Object Relational Mapping，对象关系映射）技术。</p>
<p>JPA 规范中定义了一些既定的概念和约定，集中包含在 javax.persistence 包中，常见的如对实体（Entity）定义、实体标识定义、实体与实体之间的关联关系定义，以及 09 讲中介绍的 JPQL 定义等，关于这些定义及其使用方法，一会儿我们会详细展开说明。</p>
<p>与 JDBC 规范一样，JPA 规范也有一大批实现工具和框架，极具代表性的如老牌的 Hibernate 及今天我们将介绍的 Spring Data JPA。</p>
<p>为了演示基于 Spring Data JPA 的整个开发过程，我们将在 SpringCSS 案例中专门设计和实现一套独立的领域对象和 Repository，接下来我们一起来看下。</p>
<h4>实体类注解</h4>
<p>我们知道 order-service 中存在两个主要领域对象，即 Order 和 Goods。为了与前面课时介绍的领域对象有所区分，本节课我们重新创建两个领域对象，分别命名为 JpaOrder 和 JpaGoods，它们就是 JPA 规范中的实体类。</p>
<p>我们先来看下相对简单的 JpaGoods，这里我们把 JPA 规范的相关类的引用罗列在了一起，JpaGoods 定义如下代码所示：</p>
<pre><code>import javax.persistence.Entity;

import javax.persistence.GeneratedValue;

import javax.persistence.GenerationType;

import javax.persistence.Id;

import javax.persistence.Table;

 

@Entity

@Table(name=&quot;goods&quot;)

public class JpaGoods {

    

    @Id

    @GeneratedValue(strategy = GenerationType.IDENTITY)

    private Long id;    

    private String goodsCode;

    private String goodsName;

    private Float price;    

    //省略 getter/setter

}
</code></pre>
<p>JpaGoods 中使用了 JPA 规范中用于定义实体的几个注解：最重要的 @Entity 注解、用于指定表名的 @Table 注解、用于标识主键的 @Id 注解，以及用于标识自增数据的 @GeneratedValue 注解，这些注解都比较直白，在实体类上直接使用即可。</p>
<p>接下来，我们看下比较复杂的 JpaOrder，定义如下代码所示：</p>
<pre><code>@Entity

@Table(name=&quot;`order`&quot;)

public class JpaOrder implements Serializable {

    private static final long serialVersionUID = 1L;

    

    @Id

    @GeneratedValue(strategy = GenerationType.IDENTITY)

    private Long id;

    private String orderNumber;

    private String deliveryAddress;

 

    @ManyToMany(targetEntity=JpaGoods.class)

    @JoinTable(name = &quot;order_goods&quot;, joinColumns = @JoinColumn(name = &quot;order_id&quot;, referencedColumnName = &quot;id&quot;), inverseJoinColumns = @JoinColumn(name = &quot;goods_id&quot;, referencedColumnName = &quot;id&quot;))

    private List&lt;JpaGoods&gt; goods = new ArrayList&lt;&gt;();

 

    //省略 getter/setter

}
</code></pre>
<p>这里除了引入了常见的一些注解，还引入了 @ManyToMany 注解，它表示 order 表与 goods 表中数据的关联关系。</p>
<p>在JPA 规范中，共提供了 one-to-one、one-to-many、many-to-one、many-to-many 这 4 种映射关系，它们分别用来处理一对一、一对多、多对一，以及多对多的关联场景。</p>
<p>针对 order-service 这个业务场景，我们设计了一张 order_goods 中间表存储 order 与 goods 表中的主键关系，且使用了 @ManyToMany 注解定义 many-to-many 这种关联关系，也使用了 @JoinTable 注解指定 order_goods 中间表，并通过 joinColumns 和 inverseJoinColumns 注解分别指定中间表中的字段名称以及引用两张主表中的外键名称。</p>
<h4>定义 Repository</h4>
<p>定义完实体对象后，我们再来提供 Repository 接口，这一步的操作非常简单，OrderJpaRepository 的定义如下代码所示：</p>
<pre><code>@Repository(&quot;orderJpaRepository&quot;)

public interface OrderJpaRepository extends JpaRepository&lt;JpaOrder, Long&gt;

{

}
</code></pre>
<p>从上面代码中我们发现，<strong>OrderJpaRepository 是一个继承了 JpaRepository 接口的空接口，基于 09 讲的介绍，我们知道 OrderJpaRepository 实际上已经具备了访问数据库的基本 CRUD 功能。</strong></p>
<h4>使用 Spring Data JPA 访问数据库</h4>
<p>有了上面定义的 JpaOrder 和 JpaGoods 实体类，以及 OrderJpaRepository 接口，我们已经可以实现很多操作了。</p>
<p>比如我们想通过 Id 获取 Order 对象，首先可以通过构建一个 JpaOrderService 直接注入 OrderJpaRepository 接口，如下代码所示：</p>
<pre><code>@Service

public class JpaOrderService {

 

    @Autowired

    private OrderJpaRepository orderJpaRepository;

 

    public JpaOrder getOrderById(Long orderId) {

 

        return orderJpaRepository.getOne(orderId);

    }

}
</code></pre>
<p>然后，我们再通过构建一个 Controller 类嵌入上述方法，并通过 HTTP 请求查询 Id 为 1 的 JpaOrder 对象，获得的结果如下代码所示：</p>
<pre><code>{

    &quot;id&quot;: 1,

    &quot;orderNumber&quot;: &quot;Order10001&quot;,

    &quot;deliveryAddress&quot;: &quot;test_address1&quot;,

    &quot;goods&quot;: [

        {

            &quot;id&quot;: 1,

            &quot;goodsCode&quot;: &quot;GoodsCode1&quot;,

            &quot;goodsName&quot;: &quot;GoodsName1&quot;,

            &quot;price&quot;: 100.0

        },

        {

            &quot;id&quot;: 2,

            &quot;goodsCode&quot;: &quot;GoodsCode2&quot;,

            &quot;goodsName&quot;: &quot;GoodsName2&quot;,

            &quot;price&quot;: 200.0

        }

    ]

}
</code></pre>
<p>请注意，这里我们不仅获取了 order 表中的订单基础数据，还同时获取了 goods 表中的商品数据，这种效果是如何实现的呢？是因为在 JpaOrder 对象中，我们添加了 @ManyToMany 注解，该注解会自动从 order_goods 表中获取商品主键信息，并从 goods 表中获取商品详细信息。</p>
<p>了解了使用 Spring Data JPA 实现关系型数据库访问的过程，并对比《数据访问：如何使用 JdbcTemplate 访问关系型数据库？》中通过 JdbcTemplate 获取这部分数据的实现过程，我们发现使用 Spring Data JPA 更简单。</p>
<p><strong>在多样化查询实现过程中，我们不仅可以使用 JpaRepository 中默认集成的各种 CRUD 方法，还可以使用 09 讲中介绍的 @Query 注解、方法名衍生查询等。今天，我们还将同时引入 QueryByExample 和 Specification 这两种机制来丰富多样化查询方式。</strong></p>
<h4>使用 @Query 注解</h4>
<p>使用 @Query 注解实现查询的示例如下代码所示：</p>
<pre><code>@Repository(&quot;orderJpaRepository&quot;)

public interface OrderJpaRepository extends JpaRepository&lt;JpaOrder, Long&gt;

{

 

    @Query(&quot;select o from JpaOrder o where o.orderNumber = ?1&quot;)

    JpaOrder getOrderByOrderNumberWithQuery(String orderNumber);

}
</code></pre>
<p>这里，我们使用了 JPQL 根据 OrderNumber 查询订单信息。JPQL 的语法与 SQL 语句非常类似，09 讲中我们对 JPQL 进行了讨论，这里我们不再赘述，你可以前往回顾。</p>
<p>说到 @Query 注解，JPA 中还提供了一个 @NamedQuery 注解对 @Query 注解中的语句进行命名。@NamedQuery 注解的使用方式如下代码所示：</p>
<pre><code>@Entity

@Table(name = &quot;`order`&quot;)

@NamedQueries({ @NamedQuery(name = &quot;getOrderByOrderNumberWithQuery&quot;, query = &quot;select o from JpaOrder o where o.orderNumber = ?1&quot;) })

public class JpaOrder implements Serializable {
</code></pre>
<p>在上述示例中，我们在实体类 JpaOrder 上添加了一个 @NamedQueries 注解，该注解可以将一批 @NamedQuery 注解整合在一起使用。同时，我们还使用了 @NamedQuery 注解定义了一个“getOrderByOrderNumberWithQuery”查询，且指定了对应的 JPQL 语句。</p>
<p><strong>如果你想使用这个命名查询，在 OrderJpaRepository 中定义与该命名一致的方法即可。</strong></p>
<h4>使用方法名衍生查询</h4>
<p>使用方法名衍生查询是最方便的一种自定义查询方式，在这过程中开发人员唯一需要做的就是在 JpaRepository 接口中定义一个符合查询语义的方法。</p>
<p>比如我们希望通过 OrderNumber 查询订单信息，那么可以提供如下代码所示的接口定义：</p>
<pre><code>@Repository(&quot;orderJpaRepository&quot;)

public interface OrderJpaRepository extends JpaRepository&lt;JpaOrder, Long&gt;

{

    JpaOrder getOrderByOrderNumber(String orderNumber);

}
</code></pre>
<p>通过 getOrderByOrderNumber 方法后，我们就可以自动根据 OrderNumber 获取订单详细信息了。</p>
<h4>使用 QueryByExample 机制</h4>
<p>接下来我们将介绍另一种强大的查询机制，即 QueryByExample（QBE）机制。</p>
<p>针对 JpaOrder 对象，假如我们希望根据 OrderNumber 及 DeliveryAddress 中的一个或多个条件进行查询，按照方法名衍生查询的方式构建查询方法后，得到如下代码所示的方法定义：</p>
<pre><code>List&lt;JpaOrder&gt; findByOrderNumberAndDeliveryAddress (String 

	orderNumber, String deliveryAddress);
</code></pre>
<p>如果查询条件中使用的字段非常多，上面这个方法名可能非常长，且还需要设置一批参数，这种查询方法定义显然存在缺陷。</p>
<p>因为不管查询条件有多少个，我们都需要把所有参数进行填充，哪怕部分参数并没有被用到。而且，如果将来我们需要再添加一个新的查询条件，该方法必须做调整，从扩展性上讲也存在设计缺陷。为了解决这些问题，我们便可以引入 QueryByExample 机制。</p>
<p>QueryByExample 可以翻译为按示例查询，是一种用户友好的查询技术。它允许我们动态创建查询，且不需要编写包含字段名称的查询方法，也就是说按示例查询不需要使用特定的数据库查询语言来编写查询语句。</p>
<p>从组成结构上讲，QueryByExample 包括 Probe、ExampleMatcher 和 Example 这三个基本组件。其中， Probe 包含对应字段的实例对象，ExampleMatcher 携带有关如何匹配特定字段的详细信息，相当于匹配条件，Example 则由 Probe 和 ExampleMatcher 组成，用于构建具体的查询操作。</p>
<p>现在，我们基于 QueryByExample 机制重构根据 OrderNumber 查询订单的实现过程。</p>
<p>首先，我们需要在 OrderJpaRepository 接口的定义中继承 QueryByExampleExecutor 接口，如下代码所示：</p>
<pre><code>@Repository(&quot;orderJpaRepository&quot;)

public interface OrderJpaRepository extends JpaRepository&lt;JpaOrder, Long&gt;, QueryByExampleExecutor&lt;JpaOrder&gt; {
</code></pre>
<p>然后，我们在 JpaOrderService 中实现如下代码所示的 getOrderByOrderNumberByExample 方法：</p>
<pre><code>public JpaOrder getOrderByOrderNumberByExample(String orderNumber) {

        JpaOrder order = new JpaOrder();

        order.setOrderNumber(orderNumber);

 

        ExampleMatcher matcher = ExampleMatcher.matching().withIgnoreCase()

                .withMatcher(&quot;orderNumber&quot;, GenericPropertyMatchers.exact()).withIncludeNullValues();

 

        Example&lt;JpaOrder&gt; example = Example.of(order, matcher);

 

        return orderJpaRepository.findOne(example).orElse(new JpaOrder());

}
</code></pre>
<p>上述代码中，我们首先构建了一个 ExampleMatcher 对象用于初始化匹配规则，然后通过传入一个 JpaOrder 对象实例和 ExampleMatcher 实例构建了一个 Example 对象，最后通过 QueryByExampleExecutor 接口中的 findOne() 方法实现了 QueryByExample 机制。</p>
<h4>使用 Specification 机制</h4>
<p>本节课中，最后我们想介绍的查询机制是 Specification 机制。</p>
<p>先考虑这样一种场景，比如我们需要查询某个实体，但是给定的查询条件不固定，此时该怎么办？这时我们通过动态构建相应的查询语句即可，而在 Spring Data JPA 中可以通过 JpaSpecificationExecutor 接口实现这类查询。相比使用 JPQL 而言，使用 Specification 机制的优势是类型安全。</p>
<p>继承了 JpaSpecificationExecutor 的 OrderJpaRepository 定义如下代码所示：</p>
<pre><code>@Repository(&quot;orderJpaRepository&quot;)

public interface OrderJpaRepository extends JpaRepository&lt;JpaOrder, Long&gt;,     JpaSpecificationExecutor&lt;JpaOrder&gt;{
</code></pre>
<p>对于 JpaSpecificationExecutor 接口而言，它背后使用的就是 Specification 接口，且 Specification 接口核心方法就一个，我们可以简单地理解该接口的作用就是构建查询条件，如下代码所示：</p>
<pre><code>Predicate toPredicate(Root&lt;T&gt; root, CriteriaQuery&lt;?&gt; query, CriteriaBuilder criteriaBuilder);
</code></pre>
<p>其中 Root 对象代表所查询的根对象，我们可以通过 Root 获取实体的属性，CriteriaQuery 代表一个顶层查询对象，用来实现自定义查询，而 CriteriaBuilder 用来构建查询条件。</p>
<p>基于 Specification 机制，我们同样对根据 OrderNumber 查询订单的实现过程进行重构，重构后的 getOrderByOrderNumberBySpecification 方法如下代码所示：</p>
<pre><code>public JpaOrder getOrderByOrderNumberBySpecification(String orderNumber) {

        JpaOrder order = new JpaOrder();

        order.setOrderNumber(orderNumber);

 

        @SuppressWarnings(&quot;serial&quot;)

        Specification&lt;JpaOrder&gt; spec = new Specification&lt;JpaOrder&gt;() {

            @Override

            public Predicate toPredicate(Root&lt;JpaOrder&gt; root, CriteriaQuery&lt;?&gt; query, CriteriaBuilder cb) {

                Path&lt;Object&gt; orderNumberPath = root.get(&quot;orderNumber&quot;);

              

                Predicate predicate = cb.equal(orderNumberPath, orderNumber);

                return predicate;

            }

        };

 

        return orderJpaRepository.findOne(spec).orElse(new JpaOrder());     

}
</code></pre>
<p>从上面示例中可以看到，在 toPredicate 方法中，首先我们从 root 对象中获取了“orderNumber”属性，然后通过 cb.equal 方法将该属性与传入的 orderNumber 参数进行了比对，从而实现了查询条件的构建过程。</p>
<h3>小结与预告</h3>
<p>10 讲中，我们主要对通过 Spring Data JPA 进行数据操作的方法和技巧做了一一介绍。</p>
<p>在 Spring Boot 中，我极力推荐使用 Spring Data JPA 实现对关系型数据库访问，因为它不仅具有 ORM 框架的通用功能，同时还添加了 QueryByExample 和 Specification 机制等扩展性功能，应用上简单而高效。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="09&#32;&#32;数据抽象：Spring&#32;Data&#32;如何对数据访问过程进行统一抽象？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="11&#32;&#32;服务发布：如何构建一个&#32;RESTful&#32;风格的&#32;Web&#32;服务？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434d1559f070ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
