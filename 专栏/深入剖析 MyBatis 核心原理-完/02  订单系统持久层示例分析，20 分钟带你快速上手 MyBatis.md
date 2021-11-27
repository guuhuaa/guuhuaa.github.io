<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>02  订单系统持久层示例分析，20 分钟带你快速上手 MyBatis.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;领略&#32;MyBatis&#32;设计思维，突破持久化技术瓶颈.md">00 开篇词  领略 MyBatis 设计思维，突破持久化技术瓶颈.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;常见持久层框架赏析，到底是什么让你选择&#32;MyBatis？.md">01  常见持久层框架赏析，到底是什么让你选择 MyBatis？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="02&#32;&#32;订单系统持久层示例分析，20&#32;分钟带你快速上手&#32;MyBatis.md">02  订单系统持久层示例分析，20 分钟带你快速上手 MyBatis.md</a>
                    

                </li>
                <li>

                    
                    <a href="03&#32;&#32;MyBatis&#32;源码环境搭建及整体架构解析.md">03  MyBatis 源码环境搭建及整体架构解析.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;MyBatis&#32;反射工具箱：带你领略不一样的反射设计思路.md">04  MyBatis 反射工具箱：带你领略不一样的反射设计思路.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;数据库类型体系与&#32;Java&#32;类型体系之间的“爱恨情仇”.md">05  数据库类型体系与 Java 类型体系之间的“爱恨情仇”.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;日志框架千千万，MyBatis&#32;都能兼容的秘密是什么？.md">06  日志框架千千万，MyBatis 都能兼容的秘密是什么？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;深入数据源和事务，把握持久化框架的两个关键命脉.md">07  深入数据源和事务，把握持久化框架的两个关键命脉.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;Mapper&#32;文件与&#32;Java&#32;接口的优雅映射之道.md">08  Mapper 文件与 Java 接口的优雅映射之道.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;基于&#32;MyBatis&#32;缓存分析装饰器模式的最佳实践.md">09  基于 MyBatis 缓存分析装饰器模式的最佳实践.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;鸟瞰&#32;MyBatis&#32;初始化，把握&#32;MyBatis&#32;启动流程脉络（上）.md">10  鸟瞰 MyBatis 初始化，把握 MyBatis 启动流程脉络（上）.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;鸟瞰&#32;MyBatis&#32;初始化，把握&#32;MyBatis&#32;启动流程脉络（下）.md">11  鸟瞰 MyBatis 初始化，把握 MyBatis 启动流程脉络（下）.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;深入分析动态&#32;SQL&#32;语句解析全流程（上）.md">12  深入分析动态 SQL 语句解析全流程（上）.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;深入分析动态&#32;SQL&#32;语句解析全流程（下）.md">13  深入分析动态 SQL 语句解析全流程（下）.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;探究&#32;MyBatis&#32;结果集映射机制背后的秘密（上）.md">14  探究 MyBatis 结果集映射机制背后的秘密（上）.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;探究&#32;MyBatis&#32;结果集映射机制背后的秘密（下）.md">15  探究 MyBatis 结果集映射机制背后的秘密（下）.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;StatementHandler：参数绑定、SQL&#32;执行和结果映射的奠基者.md">16  StatementHandler：参数绑定、SQL 执行和结果映射的奠基者.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;Executor&#32;才是执行&#32;SQL&#32;语句的幕后推手（上）.md">17  Executor 才是执行 SQL 语句的幕后推手（上）.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;Executor&#32;才是执行&#32;SQL&#32;语句的幕后推手（下）.md">18  Executor 才是执行 SQL 语句的幕后推手（下）.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;深入&#32;MyBatis&#32;内核与业务逻辑的桥梁——接口层.md">19  深入 MyBatis 内核与业务逻辑的桥梁——接口层.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;插件体系让&#32;MyBatis&#32;世界更加精彩.md">20  插件体系让 MyBatis 世界更加精彩.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;深挖&#32;MyBatis&#32;与&#32;Spring&#32;集成底层原理.md">21  深挖 MyBatis 与 Spring 集成底层原理.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;基于&#32;MyBatis&#32;的衍生框架一览.md">22  基于 MyBatis 的衍生框架一览.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;结束语&#32;&#32;会使用只能默默“搬砖”，懂原理才能快速晋升.md">23 结束语  会使用只能默默“搬砖”，懂原理才能快速晋升.md</a>

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
                        <div><h1>02  订单系统持久层示例分析，20 分钟带你快速上手 MyBatis</h1>
<p>在开始深入分析 MyBatis 核心架构以及具体代码实现之前，我先通过一个示例来帮助你快速了解 MyBatis 中的常见概念以及其基础使用方法。</p>
<p>这里我会以<strong>一个简易订单系统的持久化层</strong>为例进行讲解，整体的讲解逻辑是这样的：</p>
<ul>
<li>首先介绍订单系统 domain 层的设计，了解如何将业务概念抽象成 Java 类；</li>
<li>接下来介绍数据库表的设计，同时说明关系型的数据库表与面向对象模型的类之间的映射关系；</li>
<li>随后介绍订单系统的 DAO 接口层，DAO 接口层是操作数据的最小化单元，也是读写数据库的地基；</li>
<li>最后再简单提供了一个 Service 层和测试用例，用来检测前面的代码实现是否能正常工作。</li>
</ul>
<p>现在<strong>几乎所有的 Java 工程都会使用 Maven 来管理 jar 包依赖</strong>，所以我们首先创建一个 Maven 项目，然后在 pom.xml 中添加如下 jar 依赖，这些 jar 包都是订单示例系统必不可少的依赖：</p>
<pre><code>&lt;dependencies&gt;

  &lt;!--MyBatis依赖--&gt;

  &lt;dependency&gt;

      &lt;groupId&gt;org.mybatis&lt;/groupId&gt;

      &lt;artifactId&gt;mybatis&lt;/artifactId&gt;

      &lt;version&gt;3.5.6&lt;/version&gt;

  &lt;/dependency&gt;

  &lt;!--MySQL JDBC依赖，用来连接数据库--&gt;

  &lt;dependency&gt;

      &lt;groupId&gt;mysql&lt;/groupId&gt;

      &lt;artifactId&gt;mysql-connector-java&lt;/artifactId&gt;

      &lt;version&gt;8.0.15&lt;/version&gt;

  &lt;/dependency&gt;

  &lt;!--Guava依赖--&gt;

  &lt;dependency&gt;

      &lt;groupId&gt;com.google.guava&lt;/groupId&gt;

      &lt;artifactId&gt;guava&lt;/artifactId&gt;

      &lt;version&gt;19.0&lt;/version&gt;

  &lt;/dependency&gt;

  &lt;!--Junit依赖，用来执行单元测试--&gt;

  &lt;dependency&gt;

      &lt;groupId&gt;junit&lt;/groupId&gt;

      &lt;artifactId&gt;junit&lt;/artifactId&gt;

      &lt;version&gt;4.10&lt;/version&gt;

      &lt;scope&gt;test&lt;/scope&gt;

  &lt;/dependency&gt;

&lt;/dependencies&gt;
</code></pre>
<h3>domain 设计</h3>
<p>在业务系统的开发中，<strong>domain 层的主要目的就是将业务上的概念抽象成面向对象模型中的类</strong>，这些类是业务系统运作的基础。在我们的简易订单系统中，有用户、地址、订单、订单条目和商品这五个核心的概念。</p>
<p>订单系统中 domain 层的设计，如下图所示：</p>
<p><img src="assets/CgqCHmAJK4eAXeXQAACJoVb_GUk600.png" alt="Drawing 0.png" /></p>
<p>简易订单系统 domain 层设计图</p>
<p>在上图中，<strong>Customer 类抽象的是电商平台中的用户</strong>，其中记录了用户的唯一标识（id 字段）、姓名（name 字段）以及手机号（phone 字段），另外，还记录了当前用户添加的全部送货地址。</p>
<p><strong>Address 类抽象了用户的送货地址</strong>，其中记录了街道（street 字段）、城市（city 字段）、国家（country 字段）等信息，还维护了一个 Customer 类型的引用，指向所属的用户。</p>
<p><strong>Order 类抽象的是电商平台中的订单</strong>，记录了订单的唯一标识（id 字段）、订单创建时间（createTime 字段），其中通过 customer 字段（Customer 类型）指向了订单关联的用户，通过 deliveryAddress 字段（Address 类型）指向了该订单的送货地址。另外，还可以通过 orderItems 集合（List 集合）记录订单内的具体条目。</p>
<p><strong>OrderItem 类抽象了订单中的购物条目</strong>，记录了购物条目的唯一标识（id 字段），其中 product 字段（Product 类型）指向了该购物条目中具体购买的商品，amount 字段记录购买商品的个数，price 字段则是该 OrderItem 的总金额（即 Product.price * amount），Order 订单的总价格（totalPrice 字段）则是由其中全部 OrderItem 的 price 累加得到的。注意，这里的 OrderItem 总金额以及 Order 总金额，都不会持久化到数据，而是实时计算得到的。</p>
<p><strong>Product 类抽象了电商平台中商品的概念</strong>，其中记录了商品的唯一标识（id 字段）、商品名称（name 字段）、商品描述（description 字段）以及商品价格（price 字段）。</p>
<p>结合前面的介绍以及类图分析，你可以看到：</p>
<ul>
<li>通过 Customer.addresses 以及 Address.customer 这两个属性，维护了 Customer 与 Address 之间<strong>一对多</strong>关系；</li>
<li>通过 Order.customer 属性，维护了 Customer 与 Order 之间的<strong>一对多</strong>关系；</li>
<li>通过 Order.deliveryAddress 属性，维护了 Order 与 Address 之间的<strong>一对一</strong>关系；</li>
<li>通过 OrderItem.orderId 属性，维护了 Order 与 OrderItem 之间的<strong>一对多</strong>关系；</li>
<li>通过 OrderItem.product 属性，维护了 OrderItem 与 Product 之间的<strong>一对一</strong>关系。</li>
</ul>
<h3>数据库表设计</h3>
<p>介绍完 domain 层的设计，下面我们再来看对应的数据库表设计，如下图所示：</p>
<p><img src="assets/CgqCHmAJK5mAIH-vAAB6RUBTHlw421.png" alt="Drawing 1.png" /></p>
<p>简易订单系统数据库表设计</p>
<p>与前面的domain 层设计图相比，其中的各项是可以一一对应起来的。</p>
<ul>
<li>t_customer 表对应 Customer 类，t_product 表对应 Product 类。</li>
<li>t_address 表对应 Address 类，其中 customer_id 列作为外键指向 t_customer.id，实现了 Customer 与 Address 的一对多关系。</li>
<li>t_order_item 表对应 OrderItem 类，其中 product_id 列作为外键指向 t_product.id，实现了 OrderItem 与 Product 的一对一关系；order_id 列作为外键指向 t_order.id，实现了 Order 与 OrderItem 的一对多关系。</li>
<li>t_order 表对应 Order 类，其中的 customer_id 列指向 t_customer.id，实现了 Customer 与 Order 的一对多关系；address_id 列指向 t_address.id，实现了 Order 与 Address 的一对一关系。</li>
</ul>
<p>上述表中的其他字段与 domain 层中对应类中的字段也是一一对应，这里就不再重复了。</p>
<h3>DAO 层</h3>
<p><strong>DAO 层主要是负责与持久化存储进行交互，完成数据持久化的相关工作</strong>，这里我们就介绍一下 如何使用 MyBatis 来开发 Java 应用中的持久层。</p>
<p>在 DAO 层中，需要先根据需求确定 DAO 层的基本能力，一般情况下，是针对每个 domain 类提供最基础的 CRUD 操作，之后在 DAO 层之上的 Service 层，就可以直接使用 DAO 层的接口，而无须关心底层使用的是数据库还是其他存储，也无须关心读写数据使用的是 SQL 语句还是其他查询语句，这就能够实现业务逻辑和存储的解耦。</p>
<h4>1. DAO 接口与实现</h4>
<p>下面，我们开始介绍简易订单系统中 DAO 接口的内容。</p>
<p>首先是 CustomerMapper 接口，其定义如下：</p>
<pre><code>public interface CustomerMapper {

    // 根据用户Id查询Customer(不查询Address)

    Customer find(long id);

    // 根据用户Id查询Customer(同时查询Address)

    Customer findWithAddress(long id);

    // 根据orderId查询Customer

    Customer findByOrderId(long orderId);

    // 持久化Customer对象

    int save(Customer customer);

}
</code></pre>
<p>定义完 CustomerMapper 接口之后，我们<strong>无须真正实现 CustomerMapper 接口，而是在 /resources/mapper 目录下配置相应的配置文件—— CustomerMapper.xml，在该文件中定义需要执行的 SQL 语句以及查询结果集的映射规则</strong>。MyBatis 底层会生成一个实现了 CustomerMapper 接口的代理对象来执行 CustomerMapper.xml 配置文件中的 SQL 语句，实现 DAO 层的功能（MyBatis 如何生成代理对象等底层原理在本课程后面会深入分析，这里就先介绍该示例系统的相关内容）。</p>
<p>CustomerMapper.xml 的具体定义如下：</p>
<pre><code>&lt;mapper namespace=&quot;org.example.dao.CustomerMapper&quot;&gt;

    &lt;!-- 定义映射规则 --&gt;

    &lt;resultMap id=&quot;customerSimpleMap&quot; type=&quot;Customer&quot;&gt;

        &lt;!--  主键映射 --&gt;

        &lt;id property=&quot;id&quot; column=&quot;id&quot;/&gt;

        &lt;!--  属性映射 --&gt;

        &lt;result property=&quot;name&quot; column=&quot;name&quot;/&gt;

        &lt;result property=&quot;phone&quot; column=&quot;phone&quot;/&gt;

    &lt;/resultMap&gt;

    &lt;!-- 定义映射规则 --&gt;

    &lt;resultMap id=&quot;customerMap&quot; type=&quot;Customer&quot;&gt;

        &lt;!--  主键映射 --&gt;

        &lt;id property=&quot;id&quot; column=&quot;id&quot;/&gt;

        &lt;!--  属性映射 --&gt;

        &lt;result property=&quot;name&quot; column=&quot;name&quot;/&gt;

        &lt;result property=&quot;phone&quot; column=&quot;phone&quot;/&gt;

        &lt;!-- 映射addresses集合，&lt;collection&gt;标签用于映射集合类的属性，实现一对多的关联关系 --&gt;

        &lt;collection property=&quot;addresses&quot; javaType=&quot;list&quot; ofType=&quot;Address&quot;&gt;

            &lt;id property=&quot;id&quot; column=&quot;address_id&quot;/&gt;

            &lt;result property=&quot;street&quot; column=&quot;street&quot;/&gt;

            &lt;result property=&quot;city&quot; column=&quot;city&quot;/&gt;

            &lt;result property=&quot;country&quot; column=&quot;country&quot;/&gt;

        &lt;/collection&gt;

    &lt;/resultMap&gt;

    &lt;!-- 定义select语句，CustomerMapper接口中的find()方法会执行该SQL，

        查询结果通过customerSimpleMap这个映射生成Customer对象--&gt;

    &lt;select id=&quot;find&quot; resultMap=&quot;customerSimpleMap&quot;&gt;

        SELECT * FROM t_customer WHERE id = #{id:INTEGER}

    &lt;/select&gt;

    &lt;!-- 定义select语句，CustomerMapper接口中的findWithAddress()方法会执行该SQL，

        查询结果通过customerMap这个映射生成Customer对象--&gt;

    &lt;select id=&quot;findWithAddress&quot; resultMap=&quot;customerMap&quot;&gt;

        SELECT c.*,a.id as address_id, a.* FROM t_customer as c join t_address as a

        on c.id = a.customer_id

        WHERE c.id = #{id:INTEGER}

    &lt;/select&gt;

    &lt;!-- CustomerMapper接口中的findByOrderId()方法会执行该SQL，

        查询结果通过customerSimpleMap这个映射生成Customer对象--&gt;

    &lt;select id=&quot;findByOrderId&quot; resultMap=&quot;customerSimpleMap&quot;&gt;

        SELECT * FROM t_customer as c join t_order as t

        on c.id = t.customer_id

        WHERE t.customer_id = #{id:INTEGER}

    &lt;/select&gt;

    &lt;!-- 定义insert语句，CustomerMapper接口中的save()方法会执行该SQL，

        数据库生成的自增id会自动填充到传入的Customer对象的id字段中--&gt;

    &lt;insert id=&quot;save&quot; keyProperty=&quot;id&quot; useGeneratedKeys=&quot;true&quot;&gt;

      insert into t_customer (id, name, phone)

      values (#{id},#{name},#{phone})

    &lt;/insert&gt;

&lt;/mapper&gt;
</code></pre>
<p>接下来，我们看一下 AddressMapper 接口的定义，它主要是针对 Address 对象的 CRUD：</p>
<pre><code>public interface AddressMapper {

    // 根据id查询Address对象

    Address find(long id);

    // 查询一个用户的全部地址信息

    List&lt;Address&gt; findAll(long customerId);

    // 查询指定订单的送货地址

    Address findByOrderId(long orderId);

    // 存储Address对象，同时会记录关联的Customer

    int save(@Param(&quot;address&quot;) Address address,

              @Param(&quot;customerId&quot;) long customerId);

}
</code></pre>
<p>AddressMapper 接口对应的 AddressMapper.xml 配置文件中，同样定义了每个方法要执行的 SQL 语句以及查询结果与 Address 对象之间的映射关系，具体定义如下：</p>
<pre><code>&lt;mapper namespace=&quot;org.example.dao.AddressMapper&quot;&gt;

    &lt;!-- find()、findAll()方法对应的&lt;select&gt;标签以及&lt;resultMap&gt;映射比较简单，这里不再展示，感兴趣的同学可以参考代码进行学习 --&gt;

    &lt;!-- 定义select语句，AddressMapper接口中的findByOrderId()方法会执行该SQL，

    查询结果通过addressMap这个映射生成Address对象--&gt;

    &lt;select id=&quot;findByOrderId&quot; resultMap=&quot;addressMap&quot;&gt;

        SELECT a.* FROM t_address as a join t_order as o

        on a.id = o.address_id

        WHERE o.address_id = #{id}

    &lt;/select&gt;

    &lt;!-- 定义insert语句，AddressMapper接口中的save()方法会执行该SQL，

        数据库生成的自增id会自动填充到传入的Address对象的id字段中--&gt;

    &lt;insert id=&quot;save&quot; keyProperty=&quot;address.id&quot; useGeneratedKeys=&quot;true&quot;&gt;

      insert into t_address (street, city, country, customer_id)

      values (#{address.street},#{address.city},#{address.country},#{customerId})

    &lt;/insert&gt;

&lt;/mapper&gt;
</code></pre>
<p>下面来看 ProductMapper 接口，其中<strong>除了根据 id 查询 Product 之外，还可以通过 name 进行模糊查询</strong>，具体定义如下：</p>
<pre><code>public interface ProductMapper {

    // 根据id查询商品信息

    Product find(long id);

    // 根据名称搜索商品信息

    List&lt;Product&gt; findByName(String name);

    // 保存商品信息

    long save(Product product);

}
</code></pre>
<p>ProductMapper 接口对应的 ProductMapper.xml 配置文件中，定义了 Product 相关的 SQL 语句以及查询结果与 Product 对象之间的映射关系。ProductMapper.xml 配置文件中定义的 SQL 语句以及 ResultMap 映射比较简单，这里不再展示，你若感兴趣的话可以参考<a href="https://github.com/xxxlxy2008/mybatisDemo">源码</a>进行学习。</p>
<p>紧接着，我们再来看 OrderItemMapper 接口的定义，其中定义了 OrderItem 对象的操作，如下所示：</p>
<pre><code>public interface OrderItemMapper {

    // 根据id查询OrderItem对象

    OrderItem find(long id);

    // 查询指定的订单中的全部OrderItem

    List&lt;OrderItem&gt; findByOrderId(long orderId);

    // 保存一个OrderItem信息

    long save(@Param(&quot;orderItem&quot;)OrderItem orderItem, 

              @Param(&quot;orderId&quot;) long orderId);

}
</code></pre>
<p>与之对应的 OrderItemMapper.xml 配置文件的定义如下：</p>
<pre><code>&lt;mapper namespace=&quot;org.example.dao.OrderItemMapper&quot;&gt;

    &lt;!-- 定义t_order_item与OrderItem对象之间的映射关系--&gt;

    &lt;resultMap id=&quot;orderItemtMap&quot; type=&quot;OrderItem&quot;&gt;

        &lt;id property=&quot;id&quot; column=&quot;id&quot;/&gt;

        &lt;result property=&quot;amount&quot; column=&quot;amount&quot;/&gt;

        &lt;result property=&quot;orderId&quot; column=&quot;order_id&quot;/&gt;

        &lt;!--映射OrderItem关联的Product对象，&lt;association&gt;标签用于实现一对一的关联关系--&gt;

        &lt;association property=&quot;product&quot; javaType=&quot;Product&quot;&gt;

            &lt;id property=&quot;id&quot; column=&quot;product_id&quot;/&gt;

            &lt;result property=&quot;name&quot; column=&quot;name&quot;/&gt;

            &lt;result property=&quot;description&quot; column=&quot;description&quot;/&gt;

            &lt;result property=&quot;price&quot; column=&quot;price&quot;/&gt;

        &lt;/association&gt;

    &lt;/resultMap&gt;

    &lt;!-- 定义select语句，OrderItemMapper接口中的find()方法会执行该SQL，

        查询结果通过orderItemtMap这个映射生成OrderItem对象--&gt;

    &lt;select id=&quot;find&quot; resultMap=&quot;orderItemtMap&quot;&gt;

        SELECT i.*,p.*,p.id as product_id FROM t_order_item as i join t_product as p

        on i.product_id = p.id WHERE id = #{id:INTEGER}

    &lt;/select&gt;

    &lt;!-- 定义select语句，OrderItemMapper接口中的findAll()方法会执行该SQL，

        查询结果通过orderItemtMap这个映射生成OrderItem对象--&gt;

    &lt;select id=&quot;findByOrderId&quot; resultMap=&quot;orderItemtMap&quot;&gt;

        SELECT i.*,p.* FROM t_order_item as i join t_product as p

        on i.product_id = p.id WHERE i.order_id = #{order_id:INTEGER}

    &lt;/select&gt;

    &lt;!-- 定义insert语句，OrderItemMapper接口中的save()方法会执行该SQL，

        数据库生成的自增id会自动填充到传入的OrderItem对象的id字段中--&gt;

    &lt;insert id=&quot;save&quot; keyProperty=&quot;orderItem.id&quot; useGeneratedKeys=&quot;true&quot;&gt;

      insert into t_order_item (amount, product_id, order_id)

      values (#{orderItem.amount}, #{orderItem.product.id}, #{orderId})

    &lt;/insert&gt;

&lt;/mapper&gt;
</code></pre>
<p>最后来看 OrderMapper 接口的定义，其中定义了查询、存储 Order 对象的相关方法，具体如下所示：</p>
<pre><code>public interface OrderMapper {

    // 根据订单Id查询

    Order find(long id);

    // 查询一个用户一段时间段内的订单列表

    List&lt;Order&gt; findByCustomerId(long customerId, long startTime, long endTime);

    // 保存一个订单

    long save(Order order);

}
</code></pre>
<p>与 OrderMapper 接口对应的 SQL 语句定义在 OrderMapper.xml 配置文件中，如下所示：</p>
<pre><code>&lt;mapper namespace=&quot;org.example.dao.OrderMapper&quot;&gt;

    &lt;!-- 定义t_order表查询记录与Order对象之间映射 --&gt;

    &lt;resultMap id=&quot;orderMap&quot; type=&quot;Order&quot;&gt;

        &lt;!-- 主键映射 --&gt;

        &lt;id property=&quot;id&quot; column=&quot;id&quot;/&gt;

        &lt;!-- 属性映射 --&gt;

        &lt;result property=&quot;createTime&quot; column=&quot;create_time&quot;/&gt;

        &lt;!-- 映射customer字段 --&gt;

        &lt;association property=&quot;customer&quot; javaType=&quot;Customer&quot;&gt;

            &lt;id property=&quot;id&quot; column=&quot;customer_id&quot;/&gt;

        &lt;/association&gt;

        &lt;!-- 映射deliveryAddress字段 --&gt;

        &lt;association property=&quot;deliveryAddress&quot; javaType=&quot;Address&quot;&gt;

            &lt;id property=&quot;id&quot; column=&quot;address_id&quot;/&gt;

        &lt;/association&gt;

        &lt;!-- 这里并没有映射orderItems集合--&gt;

    &lt;/resultMap&gt;

    &lt;!-- 定义select语句，OrderMapper接口中的find()方法会执行该SQL，

        查询结果通过orderMap这个映射生成Order对象--&gt;

    &lt;select id=&quot;find&quot; resultMap=&quot;orderMap&quot;&gt;

        SELECT * FROM t_order WHERE id = #{id:INTEGER}

    &lt;/select&gt;

    &lt;!-- 定义select语句，OrderMapper接口中的findByCustomerId()方法会执行该SQL，

        查询结果通过orderMap这个映射生成Order对象。注意这里大于号、小于号在XML中的写法--&gt;

    &lt;select id=&quot;findByCustomerId&quot; resultMap=&quot;orderMap&quot;&gt;

        SELECT * FROM t_order WHERE customer_id = #{id}

        and create_date_time &lt;![CDATA[ &gt;= ]]&gt; #{startTime}

        and  create_date_time &lt;![CDATA[ &lt;= ]]&gt; #{endTime}

    &lt;/select&gt;

    &lt;!-- 定义insert语句，OrderMapper接口中的save()方法会执行该SQL，

        数据库生成的自增id会自动填充到传入的Order对象的id字段中--&gt;

    &lt;insert id=&quot;save&quot; keyProperty=&quot;id&quot; useGeneratedKeys=&quot;true&quot;&gt;

      insert into t_order (customer_id, address_id, create_time)

      values (#{customer.id}, #{deliveryAddress.id}, #{createTime})

    &lt;/insert&gt;

&lt;/mapper&gt;
</code></pre>
<h4>2. DaoUtils 工具类</h4>
<p>在 DAO 层中，除了定义上述接口和相关实现之外，还需要管理数据库连接和事务。在订单系统中，我们<strong>使用 DaoUtils 工具类来完成 MyBatis 中 SqlSession 以及事务的相关操作</strong>，这个实现非常简单，在实践中，一般会使用专门的事务管理器来管理事务。</p>
<p>下面是 DaoUtils 工具类的核心实现：</p>
<pre><code>public class DaoUtils {

    private static SqlSessionFactory factory;

    static { // 在静态代码块中直接读取MyBatis的mybatis-config.xml配置文件

        String resource = &quot;mybatis-config.xml&quot;;

        InputStream inputStream = null;

        try {

            inputStream = Resources.getResourceAsStream(resource);

        } catch (IOException e) {

            System.err.println(&quot;read mybatis-config.xml fail&quot;);

            e.printStackTrace();

            System.exit(1);

        }

        // 加载完mybatis-config.xml配置文件之后，会根据其中的配置信息创建SqlSessionFactory对象

        factory = new SqlSessionFactoryBuilder()

                .build(inputStream);

    }

    public static &lt;R&gt; R execute(Function&lt;SqlSession, R&gt; function) {

        // 创建SqlSession

        SqlSession session = factory.openSession();

        try {

            R apply = function.apply(session);

            // 提交事务

            session.commit();

            return apply;

        } catch (Throwable t) {

            // 出现异常的时候，回滚事务

            session.rollback(); 

            System.out.println(&quot;execute error&quot;);

            throw t;

        } finally {

            // 关闭SqlSession

            session.close();

        }

    }

}
</code></pre>
<p>在 DaoUtils 中加载的 mybatis-config.xml 配置文件位于 /resource 目录下，<strong>是 MyBatis 框架配置的入口</strong>，其中配置了要连接的数据库地址、Mapper.xml 文件的位置以及一些自定义变量和别名，具体定义如下所示：</p>
<pre><code>&lt;configuration&gt;

    &lt;properties&gt; &lt;!-- 定义属性值 --&gt;

        &lt;property name=&quot;username&quot; value=&quot;root&quot;/&gt;

        &lt;property name=&quot;id&quot; value=&quot;xxx&quot;/&gt;

    &lt;/properties&gt;

    &lt;settings&gt;&lt;!-- 全局配置信息 --&gt;

        &lt;setting name=&quot;cacheEnabled&quot; value=&quot;true&quot;/&gt;

    &lt;/settings&gt;

    &lt;typeAliases&gt;

        &lt;!-- 配置别名信息，在映射配置文件中可以直接使用Customer这个别名

            代替org.example.domain.Customer这个类 --&gt;

        &lt;typeAlias type=&quot;org.example.domain.Customer&quot; alias=&quot;Customer&quot;/&gt;

        &lt;typeAlias type=&quot;org.example.domain.Address&quot; alias=&quot;Address&quot;/&gt;

        &lt;typeAlias type=&quot;org.example.domain.Order&quot; alias=&quot;Order&quot;/&gt;

        &lt;typeAlias type=&quot;org.example.domain.OrderItem&quot; alias=&quot;OrderItem&quot;/&gt;

        &lt;typeAlias type=&quot;org.example.domain.Product&quot; alias=&quot;Product&quot;/&gt;

    &lt;/typeAliases&gt;

    &lt;environments default=&quot;development&quot;&gt;

        &lt;environment id=&quot;development&quot;&gt;

            &lt;!-- 配置事务管理器的类型 --&gt;

            &lt;transactionManager type=&quot;JDBC&quot;/&gt;

            &lt;!-- 配置数据源的类型，以及数据库连接的相关信息 --&gt;

            &lt;dataSource type=&quot;POOLED&quot;&gt;

                &lt;property name=&quot;driver&quot; value=&quot;com.mysql.jdbc.Driver&quot;/&gt;

                &lt;property name=&quot;url&quot; value=&quot;jdbc:mysql://localhost:3306/test&quot;/&gt;

                &lt;property name=&quot;username&quot; value=&quot;root&quot;/&gt;

                &lt;property name=&quot;password&quot; value=&quot;xxx&quot;/&gt;

            &lt;/dataSource&gt;

        &lt;/environment&gt;

    &lt;/environments&gt;

    &lt;!-- 配置映射配置文件的位置 --&gt;

    &lt;mappers&gt;

        &lt;mapper resource=&quot;mapper/CustomerMapper.xml&quot;/&gt;

        &lt;mapper resource=&quot;mapper/AddressMapper.xml&quot;/&gt;

        &lt;mapper resource=&quot;mapper/OrderItemMapper.xml&quot;/&gt;

        &lt;mapper resource=&quot;mapper/OrderMapper.xml&quot;/&gt;

        &lt;mapper resource=&quot;mapper/ProductMapper.xml&quot;/&gt;

    &lt;/mappers&gt;

&lt;/configuration&gt;
</code></pre>
<h3>Service 层</h3>
<p>介绍完 DAO 层之后，我们接下来再来聊聊 Service 层。</p>
<p><strong>Service 层的核心职责是实现业务逻辑</strong>。在 Service 层实现的业务逻辑一般要依赖到前面介绍的 DAO 层的能力，<strong>将业务逻辑封装到 Service 层可以更方便地复用业务逻辑实现，代码会显得非常简洁，系统也会更加稳定</strong>。</p>
<p>我们先来看 CustomerService 实现，其中提供了注册用户、添加送货地址、查询用户基本信息、查询用户全部送货地址等基本功能，具体实现如下所示：</p>
<pre><code>public class CustomerService {

    // 创建一个新用户

    public long register(String name, String phone) {

        // 检查传入的name参数以及phone参数是否合法

        Preconditions.checkArgument(!Strings.isNullOrEmpty(name), &quot;name is empty&quot;);

        Preconditions.checkArgument(!Strings.isNullOrEmpty(phone), &quot;phone is empty&quot;);

        // 我们还可以完成其他业务逻辑，例如检查用户名是否重复、手机号是否重复等，这里不再展示

        return DaoUtils.execute(sqlSession -&gt; {

            // 创建Customer对象，并通过CustomerMapper.save()方法完成持久化

            CustomerMapper mapper = sqlSession.getMapper(CustomerMapper.class);

            Customer customer = new Customer();

            customer.setName(name);

            customer.setPhone(phone);

            int affected = mapper.save(customer);

            if (affected &lt;= 0) {

                throw new RuntimeException(&quot;Save Customer fail...&quot;);

            }

            return customer.getId();

        });

    }

    // 用户添加一个新的送货地址

    public long addAddress(long customerId, String street, String city, String country) {

        // 检查传入参数是否合法

        Preconditions.checkArgument(customerId &gt; 0, &quot;customerId is empty&quot;);

        Preconditions.checkArgument(!Strings.isNullOrEmpty(street), &quot;street is empty&quot;);

        Preconditions.checkArgument(!Strings.isNullOrEmpty(city), &quot;city is empty&quot;);

        Preconditions.checkArgument(!Strings.isNullOrEmpty(country), &quot;country is empty&quot;);

        // 我们还可以完成其他业务逻辑，例如检查该地址是否超出了送货范围等，这里不再展示

        return DaoUtils.execute(sqlSession -&gt; {

            // 创建Address对象并调用AddressMapper.save()方法完成持久化

            AddressMapper mapper = sqlSession.getMapper(AddressMapper.class);

            Address address = new Address();

            address.setStreet(street);

            address.setCity(city);

            address.setCountry(city);

            int affected = mapper.save(address, customerId);

            if (affected &lt;= 0) {

                throw new RuntimeException(&quot;Save Customer fail...&quot;);

            }

            return address.getId();

        });

    }

    public List&lt;Address&gt; findAllAddress(long customerId) {

        // 检查用户id参数是否合法

        Preconditions.checkArgument(customerId &gt; 0, &quot;id error&quot;);

        return DaoUtils.execute(sqlSession -&gt; {

            // 执行AddressMapper.find()方法完成查询

            AddressMapper mapper = sqlSession.getMapper(AddressMapper.class);

            return mapper.findAll(customerId);

        });

    }

    public Customer find(long id) {

        // 检查用户id参数是否合法

        Preconditions.checkArgument(id &gt; 0, &quot;id error&quot;);

        return DaoUtils.execute(sqlSession -&gt; {

            // 执行CustomerMapper.find()方法完成查询

            CustomerMapper mapper = sqlSession.getMapper(CustomerMapper.class);

            return mapper.find(id);

        });

    }

    public Customer findWithAddress(long id) {

        // 检查用户id参数是否合法

        Preconditions.checkArgument(id &gt; 0, &quot;id error&quot;);

        return DaoUtils.execute(sqlSession -&gt; {

            // 执行CustomerMapper.findWithAddress()方法完成查询

            CustomerMapper mapper = sqlSession.getMapper(CustomerMapper.class);

            return mapper.findWithAddress(id);

        });

    }

}
</code></pre>
<p>接下来看 ProductService 实现，其中提供了新增商品、根据 id 精确查询商品以及根据名称模糊查询商品的基础功能，具体实现如下：</p>
<pre><code>public class ProductService {

    // 创建商品

    public long createProduct(Product product) {

        // 检查product中的各个字段是否合法

        Preconditions.checkArgument(product != null, &quot;product is null&quot;);

        Preconditions.checkArgument(!Strings.isNullOrEmpty(product.getName()), &quot;product name is empty&quot;);

        Preconditions.checkArgument(!Strings.isNullOrEmpty(product.getDescription()), &quot;description name is empty&quot;);

        Preconditions.checkArgument(product.getPrice().compareTo(new BigDecimal(0)) &gt; 0,

                &quot;price&lt;=0 error&quot;);

        return DaoUtils.execute(sqlSession -&gt; {

            // 通过ProductMapper中的save()方法完成持久化

            ProductMapper productMapper = sqlSession.getMapper(ProductMapper.class);

            return productMapper.save(product);

        });

    }

    public Product find(long productId) {

        // 检查productId参数是否合法

        Preconditions.checkArgument(productId &gt; 0, &quot;product id error&quot;);

        return DaoUtils.execute(sqlSession -&gt; {

            // 通过ProductMapper中的find()方法精确查询Product

            ProductMapper productMapper = sqlSession.getMapper(ProductMapper.class);

            return productMapper.find(productId);

        });

    }

    public List&lt;Product&gt; find(String productName) {

        // 检查productName参数是否合法

        Preconditions.checkArgument(Strings.isNullOrEmpty(productName), &quot;product id error&quot;);

        return DaoUtils.execute(sqlSession -&gt; {

            // 根据productName模糊查询Product 

            ProductMapper productMapper = sqlSession.getMapper(ProductMapper.class);

            return productMapper.findByName(productName);

        });

    }

}
</code></pre>
<p>最后，再来看 OrderService 对 Order 订单业务的封装，其中封装了创建订单和查询订单的逻辑，另外，还提供了实时计算订单总价的功能，具体实现如下所示：</p>
<pre><code>public class OrderService {

    // 创建订单

    public long createOrder(Order order) {

        Preconditions.checkArgument(order != null, &quot;order is null&quot;);

        Preconditions.checkArgument(order.getOrderItems() != null

                        &amp;&amp; order.getOrderItems().size() &gt; 0,

                &quot;orderItems is empty&quot;);

        return DaoUtils.execute(sqlSession -&gt; {

            OrderMapper orderMapper = sqlSession.getMapper(OrderMapper.class);

            OrderItemMapper orderItemMapper = sqlSession.getMapper(OrderItemMapper.class);

            // 调用OrderMapper.save()方法完成订单的持久化

            long affected = orderMapper.save(order);

            if (affected &lt;= 0) {

                throw new RuntimeException(&quot;Save Order fail...&quot;);

            }

            long orderId = order.getId();

            for (OrderItem orderItem : order.getOrderItems()) {

                // 通过OrderItemMapper完成OrderItem的持久化

                orderItemMapper.save(orderItem, orderId);

            }

            return orderId;

        });

    }

    // 根据订单id查询订单的全部信息

    public Order find(long orderId) {

        // 检查orderId参数是否合法

        Preconditions.checkArgument(orderId &gt; 0, &quot;orderId error&quot;);

        return DaoUtils.execute(sqlSession -&gt; {

            // 查询该订单关联的全部OrderItem

            OrderItemMapper orderItemMapper = sqlSession.getMapper(OrderItemMapper.class);

            List&lt;OrderItem&gt; orderItems = orderItemMapper.findByOrderId(orderId);

            // 查询订单本身的信息

            OrderMapper orderMapper = sqlSession.getMapper(OrderMapper.class);

            Order order = orderMapper.find(orderId);

            order.setOrderItems(orderItems);

            // 计算订单总额

            order.setTotalPrice(calculateTotalPrice(order));

            // 查询订单关联的Address

            AddressMapper addressMapper = sqlSession.getMapper(AddressMapper.class);

            Address address = addressMapper.find(order.getDeliveryAddress().getId());

            order.setDeliveryAddress(address);

            return order;

        });

    }

    private BigDecimal calculateTotalPrice(Order order) {

        List&lt;OrderItem&gt; orderItems = order.getOrderItems();

        BigDecimal totalPrice = new BigDecimal(0);

        for (OrderItem orderItem : orderItems) {

            BigDecimal itemPrice = orderItem.getProduct().getPrice()

                    .multiply(new BigDecimal(orderItem.getAmount()));

            orderItem.setPrice(itemPrice);

            totalPrice.add(itemPrice);

        }

        return totalPrice;

    }

}
</code></pre>
<h3>测试用例</h3>
<p>介绍完 Service 之后，下面我们就来编写一个简单的测试用例，测试一下 Service 层和 DAO 层的实现是否正确，具体的测试用例如下所示：</p>
<pre><code>public class CustomerServiceTest {

    private static CustomerService customerService;

    private static OrderService orderService;

    private static ProductService productService;

    @Before

    public void init() { // 执行测试用例之前，初始化Service层的各个实现

        customerService = new CustomerService();

        orderService = new OrderService();

        productService = new ProductService();

    }

    @Test

    public void test01() {

        // 创建一个用户

        long customerId = customerService.register(&quot;杨四正&quot;, &quot;12345654321&quot;);

        // 为用户添加一个配送地址

        long addressId = customerService.addAddress(customerId,

                &quot;牛栏村&quot;, &quot;牛栏市&quot;, &quot;矮人国&quot;);

        System.out.println(addressId);

        // 查询用户信息以及地址信息

        Customer customer = customerService.find(customerId);

        System.out.println(customer);

        Customer customer2 = customerService.findWithAddress(customerId);

        System.out.println(customer2);

        List&lt;Address&gt; addressList = customerService.findAllAddress(customerId);

        addressList.stream().forEach(System.out::println);

        // 入库一些商品

        Product product = new Product();

        product.setName(&quot;MyBatis课程&quot;);

        product.setDescription(&quot;深入MyBatis源码的视频教程&quot;);

        product.setPrice(new BigDecimal(99));

        long productId = productService.createProduct(product);

        System.out.println(&quot;create productId:&quot; + productId);

        // 创建一个订单

        Order order = new Order();

        order.setCustomer(customer); // 买家

        order.setDeliveryAddress(addressList.get(0)); // 配送地址

        // 生成购买条目

        OrderItem orderItem = new OrderItem();

        orderItem.setAmount(20);

        orderItem.setProduct(product);

        order.setOrderItems(Lists.newArrayList(orderItem));

        long orderId = orderService.createOrder(order);

        System.out.println(&quot;create orderId:&quot; + orderId);

        Order order2 = orderService.find(orderId);

        System.out.println(order2);

    }

}
</code></pre>
<h3>总结</h3>
<p>在这一讲，我们介绍了如何使用 MyBatis 实现简易订单系统的持久化层：首先介绍了订单系统 domain 层的设计，将用户、订单、商品等业务概念抽象成了对应的 Customer、Order、Product 等 Java 类；接下来分析了订单系统持久层中数据库表的设计，主要是从关系模型角度抽象业务概念；随后又讲解了订单系统的 DAO 接口层，定义了操作数据的基本方法；最后我们提供了一个 Service 类去实现简单的业务逻辑以及相关的测试用例。</p>
<p>在本讲的末尾，我给你留一个小任务：在现有源码基础上，将各个 DAO 接口的实现调通，并编写对应的单元测试进行检查。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="01&#32;&#32;常见持久层框架赏析，到底是什么让你选择&#32;MyBatis？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="03&#32;&#32;MyBatis&#32;源码环境搭建及整体架构解析.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4356eaeaa8645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E6%B7%B1%E5%85%A5%E5%89%96%E6%9E%90%20MyBatis%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
