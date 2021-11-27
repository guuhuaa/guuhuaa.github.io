<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>07  数据访问：如何使用 JdbcTemplate 访问关系型数据库？.md</title>
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

                    <a class="current-tab" href="07&#32;&#32;数据访问：如何使用&#32;JdbcTemplate&#32;访问关系型数据库？.md">07  数据访问：如何使用 JdbcTemplate 访问关系型数据库？.md</a>
                    

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
                        <div><h1>07  数据访问：如何使用 JdbcTemplate 访问关系型数据库？</h1>
<p>06 讲我们详细介绍了 JDBC 规范的相关内容，JDBC 规范是 Java 领域中使用最广泛的数据访问标准，目前市面上主流的数据访问框架都是构建在 JDBC 规范之上。</p>
<p>因为 JDBC 是偏底层的操作规范，所以关于如何使用 JDBC 规范进行关系型数据访问的实现方式有很多（区别在于对 JDBC 规范的封装程度不同），而在 Spring 中，同样提供了 JdbcTemplate 模板工具类实现数据访问，它简化了 JDBC 规范的使用方法，今天我们将围绕这个模板类展开讨论。</p>
<h3>数据模型和 Repository 层设计</h3>
<p>引入 JdbcTemplate 模板工具类之前，我们回到 SpringCSS 案例，先给出 order-service 中的数据模型为本讲内容的展开做一些铺垫。</p>
<p>我们知道一个订单中往往涉及一个或多个商品，所以在本案例中，我们主要通过一对多的关系来展示数据库设计和实现方面的技巧。而为了使描述更简单，我们把具体的业务字段做了简化。Order 类的定义如下代码所示：</p>
<pre><code>public class Order{

    private Long id; //订单Id

    private String orderNumber; //订单编号

    private String deliveryAddress; //物流地址

    private List&lt;Goods&gt; goodsList;  //商品列表

    //省略了 getter/setter

}
</code></pre>
<p>其中代表商品的 Goods 类定义如下：</p>
<pre><code>public class Goods {

    private Long id; //商品Id

    private String goodsCode; //商品编号

    private String goodsName; //商品名称

    private Double price; //商品价格

    //省略了 getter/setter

}
</code></pre>
<p>从以上代码，我们不难看出一个订单可以包含多个商品，因此设计关系型数据库表时，我们首先会构建一个中间表来保存 Order 和 Goods 这层一对多关系。在本课程中，我们使用 MySQL 作为关系型数据库，对应的数据库 Schema 定义如下代码所示：</p>
<pre><code>DROP TABLE IF EXISTS `order`;

DROP TABLE IF EXISTS `goods`;

DROP TABLE IF EXISTS `order_goods`;

 

create table `order` (

    `id` bigint(20) NOT NULL AUTO_INCREMENT,

    `order_number` varchar(50) not null,

    `delivery_address` varchar(100) not null,

  `create_time` timestamp not null DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (`id`)

);

 

create table `goods` (

  `id` bigint(20) NOT NULL AUTO_INCREMENT,

  `goods_code` varchar(50) not null,

  `goods_name` varchar(50) not null,

  `goods_price` double not null,

  `create_time` timestamp not null DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (`id`)

);

 

create table `order_goods` (

    `order_id` bigint(20) not null,

    `goods_id` bigint(20) not null,

    foreign key(`order_id`) references `order`(`id`),

    foreign key(`goods_id`) references `goods`(`id`)

);
</code></pre>
<p>基于以上数据模型，我们将完成 order-server 中的 Repository 层组件的设计和实现。首先，我们需要设计一个 OrderRepository 接口，用来抽象数据库访问的入口，如下代码所示：</p>
<pre><code>public interface OrderRepository {

    Order addOrder(Order order);

    Order getOrderById(Long orderId);

    Order getOrderDetailByOrderNumber(String orderNumber);

}
</code></pre>
<p>这个接口非常简单，方法都是自解释的。不过请注意，这里的 OrderRepository 并没有继承任何父接口，完全是一个自定义的、独立的 Repository。</p>
<p>针对上述 OrderRepository 中的接口定义，我们将构建一系列的实现类。</p>
<ul>
<li>OrderRawJdbcRepository：使用原生 JDBC 进行数据库访问</li>
<li>OrderJdbcRepository：使用 JdbcTemplate 进行数据库访问</li>
<li>OrderJpaRepository：使用 Spring Data JPA 进行数据库访问</li>
</ul>
<p>上述实现类中的 OrderJpaRepository 我们会放到 10 讲《ORM 集成：如何使用 Spring Data JPA 访问关系型数据库？》中进行展开，而 OrderRawJdbcRepository 最基础，不是本课程的重点，因此 07 讲我们只针对 OrderRepository 中 getOrderById 方法的实现过程重点介绍，也算是对 06 讲的回顾和扩展。</p>
<p>OrderRawJdbcRepository 类中实现方法如下代码所示：</p>
<pre><code>@Repository(&quot;orderRawJdbcRepository&quot;)

public class OrderRawJdbcRepository implements OrderRepository {

 

    @Autowired

    private DataSource dataSource;

 

    @Override

    public Order getOrderById(Long orderId) {

 

        Connection connection = null;

        PreparedStatement statement = null;

        ResultSet resultSet = null;

        try {

            connection = dataSource.getConnection();

            statement = connection.prepareStatement(&quot;select id, order_number, delivery_address from `order` where id=?&quot;);

            statement.setLong(1, orderId);

            resultSet = statement.executeQuery();

            Order order = null;

            if (resultSet.next()) {

                order = new Order(resultSet.getLong(&quot;id&quot;), resultSet.getString(&quot;order_number&quot;),

                        resultSet.getString(&quot;delivery_address&quot;));

            }

            return order;

        } catch (SQLException e) {

            System.out.print(e);

        } finally {

            if (resultSet != null) {

                try {

                    resultSet.close();

                } catch (SQLException e) {

                }

            }

            if (statement != null) {

                try {

                    statement.close();

                } catch (SQLException e) {

                }

            }

            if (connection != null) {

                try {

                    connection.close();

                } catch (SQLException e) {

                }

            }

        }

        return null;

    }

    //省略其他 OrderRepository 接口方法实现

}
</code></pre>
<p>这里，值得注意的是，我们首先需要在类定义上添加 @Repository 注解，标明这是能够被 Spring 容器自动扫描的 Javabean，再在 @Repository 注解中指定这个 Javabean 的名称为&quot;orderRawJdbcRepository&quot;，方便 Service 层中根据该名称注入 OrderRawJdbcRepository 类。</p>
<p>可以看到，上述代码使用了 JDBC 原生 DataSource、Connection、PreparedStatement、ResultSet 等核心编程对象完成针对“order”表的一次查询。代码流程看起来比较简单，其实也比较烦琐，学到这里，我们可以结合上一课时的内容理解上述代码。</p>
<p>请注意，如果我们想运行这些代码，千万别忘了在 Spring Boot 的配置文件中添加对 DataSource 的定义，如下代码所示：</p>
<pre><code>spring:

  datasource:

    driver-class-name: com.mysql.cj.jdbc.Driver

    url: jdbc:mysql://127.0.0.1:3306/appointment

    username: root

    password: root
</code></pre>
<p>回顾完原生 JDBC 的使用方法，接下来就引出今天的重点，即 JdbcTemplate 模板工具类，我们来看看它如何简化数据访问操作。</p>
<h3>使用 JdbcTemplate 操作数据库</h3>
<p>要想在应用程序中使用 JdbcTemplate，首先我们需要引入对它的依赖，如下代码所示：</p>
<pre><code>&lt;dependency&gt;

    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;

    &lt;artifactId&gt;spring-boot-starter-jdbc&lt;/artifactId&gt;

&lt;/dependency&gt;
</code></pre>
<p>JdbcTemplate 提供了一系列的 query、update、execute 重载方法应对数据的 CRUD 操作。</p>
<h4>使用 JdbcTemplate 实现查询</h4>
<p>基于 SpringCSS 案例，我们先来讨论一下最简单的查询操作，并对 OrderRawJdbcRepository 中的 getOrderById 方法进行重构。为此，我们构建了一个新的 OrderJdbcRepository 类并同样实现了 OrderRepository 接口，如下代码所示：</p>
<pre><code>@Repository(&quot;orderJdbcRepository&quot;)

public class OrderJdbcRepository implements OrderRepository {

 

    private JdbcTemplate jdbcTemplate;

 

    @Autowired

    public OrderJdbcRepository(JdbcTemplate jdbcTemplate) {

        this.jdbcTemplate = jdbcTemplate;

	}

}
</code></pre>
<p>可以看到，这里通过构造函数注入了 JdbcTemplate 模板类。</p>
<p>而 OrderJdbcRepository 的 getOrderById 方法实现过程如下代码所示：</p>
<pre><code>@Override

public Order getOrderById(Long orderId) {

        Order order = jdbcTemplate.queryForObject(&quot;select id, order_number, delivery_address from `order` where id=?&quot;,

                this::mapRowToOrder, orderId);

 

        return order;

}
</code></pre>
<p>显然，这里使用了 JdbcTemplate 的 queryForObject 方法执行查询操作，该方法传入目标 SQL、参数以及一个 RowMapper 对象。其中 RowMapper 定义如下：</p>
<pre><code>public interface RowMapper&lt;T&gt; {

 

    T mapRow(ResultSet rs, int rowNum) throws SQLException;

}
</code></pre>
<p>从 mapRow 方法定义中，我们不难看出 RowMapper 的作用就是处理来自 ResultSet 中的每一行数据，并将来自数据库中的数据映射成领域对象。例如，使用 getOrderById 中用到的 mapRowToOrder 方法完成对 Order 对象的映射，如下代码所示：</p>
<pre><code>private Order mapRowToOrder(ResultSet rs, int rowNum) throws SQLException {

        return new Order(rs.getLong(&quot;id&quot;), rs.getString(&quot;order_number&quot;), rs.getString(&quot;delivery_address&quot;));

}
</code></pre>
<p>讲到这里，你可能注意到 getOrderById 方法实际上只是获取了 Order 对象中的订单部分信息，并不包含商品数据。</p>
<p>接下来，我们再来设计一个 getOrderDetailByOrderNumber 方法，根据订单编号获取订单以及订单中所包含的所有商品信息，如下代码所示：</p>
<pre><code>@Override

public Order getOrderDetailByOrderNumber(String orderNumber) {

        //获取 Order 基础信息

        Order order = jdbcTemplate.queryForObject(

                &quot;select id, order_number, delivery_address from `order` where order_number=?&quot;, this::mapRowToOrder,

                orderNumber);

 

        if (order == null)

            return order;

 

        //获取 Order 与 Goods 之间的关联关系，找到给 Order 中的所有 GoodsId

        Long orderId = order.getId();

        List&lt;Long&gt; goodsIds = jdbcTemplate.query(&quot;select order_id, goods_id from order_goods where order_id=?&quot;,

                new ResultSetExtractor&lt;List&lt;Long&gt;&gt;() {

                    public List&lt;Long&gt; extractData(ResultSet rs) throws SQLException, DataAccessException {

                        List&lt;Long&gt; list = new ArrayList&lt;Long&gt;();

                        while (rs.next()) {

                            list.add(rs.getLong(&quot;goods_id&quot;));

                        }

                        return list;

                    }

                }, orderId);

 

        //根据 GoodsId 分别获取 Goods 信息并填充到 Order 对象中

        for (Long goodsId : goodsIds) {

            Goods goods = getGoodsById(goodsId);

            order.addGoods(goods);

        }

 

        return order;

}
</code></pre>
<p>上述代码有点复杂，我们分成几个部分来讲解。</p>
<p>首先，我们获取 Order 基础信息，并通过 Order 中的 Id 编号从中间表中获取所有 Goods 的 Id 列表，通过遍历这个 Id 列表再分别获取 Goods 信息，最后将 Goods 信息填充到 Order 中，从而构建一个完整的 Order 对象。</p>
<p>这里通过 Id 获取 Goods 数据的实现方法也与 getOrderById 方法的实现过程一样，如下代码所示：</p>
<pre><code>private Goods getGoodsById(Long goodsId) {

        return jdbcTemplate.queryForObject(&quot;select id, goods_code, goods_name, price from goods where id=?&quot;,

                this::mapRowToGoods, goodsId);

}

 

private Goods mapRowToGoods(ResultSet rs, int rowNum) throws SQLException {

        return new Goods(rs.getLong(&quot;id&quot;), rs.getString(&quot;goods_code&quot;), rs.getString(&quot;goods_name&quot;),

                rs.getDouble(&quot;price&quot;));

}
</code></pre>
<h4>使用 JdbcTemplate 实现插入</h4>
<p>在 JdbcTemplate 中，我们可以通过 update 方法实现数据的插入和更新。针对 Order 和 Goods 中的关联关系，插入一个 Order 对象需要同时完成两张表的更新，即 order 表和 order_goods 表，因此插入 Order 的实现过程也分成两个阶段，如下代码所示的 addOrderWithJdbcTemplate 方法展示了这一过程：</p>
<pre><code>private Order addOrderDetailWithJdbcTemplate(Order order) {

        //插入 Order 基础信息

        Long orderId = saveOrderWithJdbcTemplate(order);

 

        order.setId(orderId);

 

        //插入 Order 与 Goods 的对应关系

        List&lt;Goods&gt; goodsList = order.getGoods();

        for (Goods goods : goodsList) {

            saveGoodsToOrderWithJdbcTemplate(goods, orderId);

        }

 

        return order;

}
</code></pre>
<p>可以看到，这里同样先是插入 Order 的基础信息，然后再遍历 Order 中的 Goods 列表并逐条进行插入。其中的 saveOrderWithJdbcTemplate 方法如下代码所示：</p>
<pre><code>private Long saveOrderWithJdbcTemplate(Order order) {

 

        PreparedStatementCreator psc = new PreparedStatementCreator() {

            @Override

            public PreparedStatement createPreparedStatement(Connection con) throws SQLException {

                PreparedStatement ps = con.prepareStatement(

                        &quot;insert into `order` (order_number, delivery_address) values (?, ?)&quot;,

                        Statement.RETURN_GENERATED_KEYS);

                ps.setString(1, order.getOrderNumber());

                ps.setString(2, order.getDeliveryAddress());

                return ps;

            }

        };

 

        KeyHolder keyHolder = new GeneratedKeyHolder();

        jdbcTemplate.update(psc, keyHolder);

 

        return keyHolder.getKey().longValue();

}
</code></pre>
<p>上述 saveOrderWithJdbcTemplate 的方法比想象中要复杂，主要原因在于我们需要在插入 order 表的同时返回数据库中所生成的自增主键，因此，这里使用了 PreparedStatementCreator 工具类封装 PreparedStatement 对象的构建过程，并在 PreparedStatement 的创建过程中设置了 Statement.RETURN_GENERATED_KEYS 用于返回自增主键。然后我们构建了一个 GeneratedKeyHolder 对象用于保存所返回的自增主键。这是使用 JdbcTemplate 实现带有自增主键数据插入的一种标准做法，你可以参考这一做法并应用到日常开发过程中。</p>
<p>至于用于插入 Order 与 Goods 关联关系的 saveGoodsToOrderWithJdbcTemplate 方法就比较简单了，直接调用 JdbcTemplate 的 update 方法插入数据即可，如下代码所示：</p>
<pre><code>private void saveGoodsToOrderWithJdbcTemplate(Goods goods, long orderId) {

        jdbcTemplate.update(&quot;insert into order_goods (order_id, goods_id) &quot; + &quot;values (?, ?)&quot;, orderId, goods.getId());

}
</code></pre>
<p>接下来，我们需要实现插入 Order 的整个流程，先实现 Service 类和 Controller 类，如下代码所示：</p>
<pre><code>@Service

public class OrderService {

 

    @Autowired

    @Qualifier(&quot;orderJdbcRepository&quot;)

    private OrderRepository orderRepository;

    public Order addOrder(Order order) {

        return orderRepository.addOrder(order);

    } 

}

 

@RestController

@RequestMapping(value=&quot;orders&quot;)

public class OrderController {

 

    @RequestMapping(value = &quot;&quot;, method = RequestMethod.POST)

    public Order addOrder(@RequestBody Order order) {

        Order result = orderService.addOrder(order);

     return result;

    }

}
</code></pre>
<p>这两个类都是直接对 orderJdbcRepository 中的方法进行封装调用，操作非常简单。然后，我们打开 Postman，并在请求消息体中输入如下内容：</p>
<pre><code>{

    &quot;orderNumber&quot; : &quot;Order10002&quot;,

    &quot;deliveryAddress&quot; : &quot;test_address2&quot;,

    &quot;goods&quot;: [

        {

            &quot;id&quot;: 1,

            &quot;goodsCode&quot;: &quot;GoodsCode1&quot;,

            &quot;goodsName&quot;: &quot;GoodsName1&quot;,

            &quot;price&quot;: 100.0

        }

    ]

}
</code></pre>
<p>通过 Postman 向<a href="http://localhost:8081/orders">http://localhost:8081/orders</a>端点发起 Post 请求后，我们发现 order 表和 order_goods 表中的数据都已经正常插入。</p>
<h4>使用 SimpleJdbcInsert 简化数据插入过程</h4>
<p>虽然通过 JdbcTemplate 的 update 方法可以完成数据的正确插入，我们不禁发现这个实现过程还是比较复杂，尤其是涉及自增主键的处理时，代码显得有点臃肿。那么有没有更加简单的实现方法呢？</p>
<p>答案是肯定的，Spring Boot 针对数据插入场景专门提供了一个 SimpleJdbcInsert 工具类，SimpleJdbcInsert 本质上是在 JdbcTemplate 的基础上添加了一层封装，提供了一组 execute、executeAndReturnKey 以及 executeBatch 重载方法来简化数据插入操作。</p>
<p>通常，我们可以在 Repository 实现类的构造函数中对 SimpleJdbcInsert 进行初始化，如下代码所示：</p>
<pre><code>private JdbcTemplate jdbcTemplate;

private SimpleJdbcInsert orderInserter;

private SimpleJdbcInsert orderGoodsInserter;

 

public OrderJdbcRepository(JdbcTemplate jdbcTemplate) {

        this.jdbcTemplate = jdbcTemplate;

        this.orderInserter = new SimpleJdbcInsert(jdbcTemplate).withTableName(&quot;`order`&quot;).usingGeneratedKeyColumns(&quot;id&quot;);

        this.orderGoodsInserter = new SimpleJdbcInsert(jdbcTemplate).withTableName(&quot;order_goods&quot;);

}
</code></pre>
<p>可以看到，这里首先注入了一个 JdbcTemplate 对象，然后我们基于 JdbcTemplate 并针对 order 表和 order_goods 表分别初始化了两个 SimpleJdbcInsert 对象 orderInserter 和 orderGoodsInserter。其中 orderInserter 中还使用了 usingGeneratedKeyColumns 方法设置自增主键列。</p>
<p>基于 SimpleJdbcInsert，完成 Order 对象的插入就非常简单了，实现方式如下所示：</p>
<pre><code>private Long saveOrderWithSimpleJdbcInsert(Order order) {

        Map&lt;String, Object&gt; values = new HashMap&lt;String, Object&gt;();

        values.put(&quot;order_number&quot;, order.getOrderNumber());

        values.put(&quot;delivery_address&quot;, order.getDeliveryAddress());

 

        Long orderId = orderInserter.executeAndReturnKey(values).longValue();

        return orderId;

}
</code></pre>
<p>我们通过构建一个 Map 对象，然后把需要添加的字段设置成一个个键值对。通过SimpleJdbcInsert 的 executeAndReturnKey 方法在插入数据的同时直接返回自增主键。同样，完成 order_goods 表的操作只需要几行代码就可以了，如下代码所示：</p>
<pre><code>private void saveGoodsToOrderWithSimpleJdbcInsert(Goods goods, long orderId) {

        Map&lt;String, Object&gt; values = new HashMap&lt;&gt;();

        values.put(&quot;order_id&quot;, orderId);

        values.put(&quot;goods_id&quot;, goods.getId());

        orderGoodsInserter.execute(values);

}
</code></pre>
<p>这里用到了 SimpleJdbcInsert 提供的 execute 方法，我们可以把这些方法组合起来对 addOrderDetailWithJdbcTemplate 方法进行重构，从而得到如下所示的 addOrderDetailWithSimpleJdbcInsert 方法：</p>
<pre><code>private Order addOrderDetailWithSimpleJdbcInsert(Order order) {

        //插入 Order 基础信息

        Long orderId = saveOrderWithSimpleJdbcInsert(order);

 

        order.setId(orderId);

        //插入 Order 与 Goods 的对应关系

        List&lt;Goods&gt; goodsList = order.getGoods();

        for (Goods goods : goodsList) {

            saveGoodsToOrderWithSimpleJdbcInsert(goods, orderId);

        }

 

        return order;

}
</code></pre>
<p>详细的代码清单可以参考课程的案例代码，你也可以基于 Postman 对重构后的代码进行尝试。</p>
<h3>小结与预告</h3>
<p>JdbcTemplate 模板工具类是一个基于 JDBC 规范实现数据访问的强大工具，是一个优秀的工具类。它对常见的 CRUD 操作做了封装并提供了一大批简化的 API。今天我们分别针对查询和插入这两大类数据操作给出了基于 JdbcTemplate 的实现方案，特别是针对插入场景，我们还引入了基于 JdbcTemplate 所构建的 SimpleJdbcInsert 简化这一操作。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="06&#32;&#32;基础规范：如何理解&#32;JDBC&#32;关系型数据库访问规范？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="08&#32;&#32;数据访问：如何剖析&#32;JdbcTemplate&#32;数据访问实现原理？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434cfefb9b70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
