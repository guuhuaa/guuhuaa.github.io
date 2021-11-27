<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>17  基于 DDD 的微服务设计演示（含支持微服务的 DDD 技术中台设计）.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;让我们把&#32;DDD&#32;的思想真正落地.md">00 开篇词  让我们把 DDD 的思想真正落地.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;DDD&#32;：杜绝软件退化的利器.md">01  DDD ：杜绝软件退化的利器.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;以电商支付功能为例演练&#32;DDD.md">02  以电商支付功能为例演练 DDD.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;DDD&#32;是如何落地到数据库设计的？.md">03  DDD 是如何落地到数据库设计的？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;领域模型是如何指导程序设计的？.md">04  领域模型是如何指导程序设计的？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;聚合、仓库与工厂：傻傻分不清楚.md">05  聚合、仓库与工厂：傻傻分不清楚.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;限界上下文：冲破微服务设计困局的利器.md">06  限界上下文：冲破微服务设计困局的利器.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;在线订餐场景中是如何开事件风暴会议的？.md">07  在线订餐场景中是如何开事件风暴会议的？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;DDD&#32;是如何解决微服务拆分难题的？.md">08  DDD 是如何解决微服务拆分难题的？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;DDD&#32;是如何落地微服务设计实现的？.md">09  DDD 是如何落地微服务设计实现的？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;微服务落地的技术实践.md">10  微服务落地的技术实践.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;解决技术改造困局的钥匙：整洁架构.md">11  解决技术改造困局的钥匙：整洁架构.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;如何设计支持快速交付的技术中台战略？.md">12  如何设计支持快速交付的技术中台战略？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;如何实现支持快速交付的技术中台设计？.md">13  如何实现支持快速交付的技术中台设计？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;如何设计支持&#32;DDD&#32;的技术中台？.md">14  如何设计支持 DDD 的技术中台？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;如何设计支持微服务的技术中台？.md">15  如何设计支持微服务的技术中台？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;基于&#32;DDD&#32;的代码设计演示（含&#32;DDD&#32;的技术中台设计）.md">16  基于 DDD 的代码设计演示（含 DDD 的技术中台设计）.md</a>

                </li>
                <li>

                    <a class="current-tab" href="17&#32;&#32;基于&#32;DDD&#32;的微服务设计演示（含支持微服务的&#32;DDD&#32;技术中台设计）.md">17  基于 DDD 的微服务设计演示（含支持微服务的 DDD 技术中台设计）.md</a>
                    

                </li>
                <li>

                    
                    <a href="18&#32;&#32;基于事件溯源的设计开发.md">18  基于事件溯源的设计开发.md</a>

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
                        <div><h1>17  基于 DDD 的微服务设计演示（含支持微服务的 DDD 技术中台设计）</h1>
<p>上一讲，我们讲解了基于 DDD 的代码设计思路，这一讲，接着来讲解我设计的、支持微服务的 DDD 技术中台的设计开发思路。</p>
<h3>单 Service 实现数据查询</h3>
<p>前面讲过通过单 Dao 实现对数据库的增删改，然而在查询的时候却是反过来，用单 Service 注入不同的 Dao，实现各种不同的查询。这样的设计也是在我以往的项目中被“逼”出来的。</p>
<p>几年前，我组织了一个大数据团队，开始<strong>大数据相关产品的设计开发</strong>。众所周知，大数据相关产品，就是运用大数据技术对海量的数据进行分析处理，并且最终的结果是通过各种报表来查询并且展现。因此，这样的项目，除了后台的各种分析处理以外，还要在前端展现各种报表，而且这些报表非常多而繁杂，动辄就是数百张之多。同时，使用这个系统的都是决策层领导，他们一会儿这样分析，一会儿那样分析，每个需求还非常急，恨不得马上就能用上。因此，我们必须具备快速开发报表的能力，而传统的从头一个一个制作报表根本来不及。</p>
<p>通过对现有报表进行反复分析，提取共性、保留个性，我发现每个报表都有许多相同或者相似的地方。<strong>每个报表在 Service 中的代码基本相同</strong>，无非就是从前端获取查询参数，然后调用 Dao 执行查询，最多再做一些翻页的操作。既然如此，那么何必要为每个功能设计 Service 呢？把它们合并到一个 Service，然后注入不同的 Dao，不就可以进行不同的查询了吗？</p>
<p>那么，这些 Dao 怎么设计呢？以往采用 MyBatis 的方式，每个 Dao 都要写一个自己的接口，然后配置一个 Mapper。然而，这些 Dao 接口都长得一模一样，只是接口名与 Mapper 不 同。此外，过去的设计，每个 Service 都对应一个 Dao，现在一个 Service 要对应很多个Dao，那用注解的方式就搞不定了。针对以上的设计难题，经过反复的调试，将架构设计成这样。</p>
<p>首先，整个系统的查询只有一个 QueryService，它有一个 QueryDao，可以注入不同的 Dao。然而，也不需要为每个 Dao 写接口，这样设计过于麻烦。用一个 QueryDaoImpl 注入不同的 Mapper，就可以做成不同的 Dao，再装配 Service，就能在 Spring 中装配成不同的 bean，做不同的查询：</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;

&lt;beans xmlns=&quot;http://www.springframework.org/schema/beans&quot; ...&gt;

 &lt;description&gt;The application context for query&lt;/description&gt;

 &lt;bean id=&quot;customerQry&quot; class=&quot;com.demo2.support.service.impl.QueryServiceImpl&quot;&gt;

  &lt;property name=&quot;queryDao&quot;&gt;

   &lt;bean class=&quot;com.demo2.support.dao.impl.QueryDaoMybatisImpl&quot;&gt;

    &lt;property name=&quot;sqlMapper&quot; value=&quot;com.demo2.trade.query.dao.CustomerMapper&quot;&gt;&lt;/property&gt;

   &lt;/bean&gt;

  &lt;/property&gt;

 &lt;/bean&gt;

&lt;/beans&gt;
</code></pre>
<p>在代码中，我们回归 xml 的形式，编写了一个 applicationContext-qry.xml。在名为customerQry 的 bean 中，class 都是 QueryServiceImpl，注入的都是QueryDaoMybatisImpl，但 sqlMapper 配置不同的 mapper，就可以进行不同的查询。</p>
<p>这个 mapper 就是 MyBatis 的 mapper，它们被放在 classpath 的 mapper 目录下（详见MyBatis 的设计开发），然后将内容按照以下的格式进行编写：</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;

&lt;!DOCTYPE mapper PUBLIC &quot;-//mybatis.org//DTD Mapper 3.0//EN&quot;

&quot;http://mybatis.org/dtd/mybatis-3-mapper.dtd&quot;&gt;

&lt;mapper namespace=&quot;com.demo2.trade.query.dao.CustomerMapper&quot;&gt;

 &lt;sql id=&quot;select&quot;&gt;

  SELECT * FROM Customer WHERE 1 = 1

 &lt;/sql&gt;

 &lt;!-- 查询条件部分 --&gt;

 &lt;sql id=&quot;conditions&quot;&gt;

  &lt;if test=&quot;id != '' and id != null&quot;&gt;

   and id = #{id}

  &lt;/if&gt;

 &lt;/sql&gt;

 &lt;!-- 翻页查询部分 --&gt;

 &lt;sql id=&quot;isPage&quot;&gt;

  &lt;if test=&quot;size != null  and size !=''&quot;&gt;

   limit #{size} offset #{firstRow} 

  &lt;/if&gt;

 &lt;/sql&gt;
 &lt;select id=&quot;query&quot; parameterType=&quot;java.util.HashMap&quot; resultType=&quot;com.demo2.trade.entity.Customer&quot;&gt;

      &lt;include refid=&quot;select&quot;/&gt;

  &lt;include refid=&quot;conditions&quot;/&gt;

  &lt;include refid=&quot;isPage&quot;/&gt;

 &lt;/select&gt;

 &lt;!-- 计算count部分 --&gt;

 &lt;select id=&quot;count&quot; parameterType=&quot;java.util.HashMap&quot; resultType=&quot;java.lang.Long&quot;&gt;

  select count(*) from (

   &lt;include refid=&quot;select&quot;/&gt;

   &lt;include refid=&quot;conditions&quot;/&gt;

  ) count

 &lt;/select&gt;

 &lt;!-- 求和计算部分 --&gt;

 &lt;select id=&quot;aggregate&quot; parameterType=&quot;java.util.HashMap&quot; resultType=&quot;java.util.HashMap&quot;&gt;

  select ${aggregation} from (

   &lt;include refid=&quot;select&quot;/&gt;

   &lt;include refid=&quot;conditions&quot;/&gt;

  ) aggregation

 &lt;/select&gt;

&lt;/mapper&gt;
</code></pre>
<p>在这段配置中，我们通常只需要修改 Select 与 Condition 部分就可以了。</p>
<ul>
<li>Select 部分是<strong>查询语句</strong>，但这部分通常是单表查询，而不采用 join 操作去 join 其他表，这样在数据量大时性能会比较差。同时，最后的 WHERE 1 = 1 是必写的，为了避免在没有查询条件时出错。</li>
<li>Condition 部分是<strong>查询条件</strong>，参数中有这个条件就加入，没有则去掉。</li>
</ul>
<p>接着，系统在后台查询时可能会执行多次：分页查询时执行一次，计算 count 时执行一次，求和计算时执行一次。但无论执行多少次，Select 与 Condition 部分只需要编写一次，从而减少了开发工作量，也避免了编写错误。</p>
<p>该 mapper 在最前面编写的 namespace，就是在 queryDao 中配置 mapper 的内容，它们必须完全一致。此外，在 query 部分的 resultType 可以写为某个领域对象，这样在<strong>查询结果集</strong>中就是这个对象的集合。</p>
<p>以上查询最好都是<strong>单表查询</strong>，那么需要 join 怎么办呢？最好采用<strong>数据补填</strong>，即在单表查询并分页的基础上，对那一页的数据执行补填。如果需要补填，那么 QueryService 就这样配置：</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;

&lt;beans xmlns=&quot;http://www.springframework.org/schema/beans&quot; ...&gt;

 &lt;description&gt;The application context for query&lt;/description&gt;

 &lt;bean id=&quot;productQry&quot; class=&quot;com.demo2.support.repository.AutofillQueryServiceImpl&quot;&gt;

  &lt;property name=&quot;queryDao&quot;&gt;

   &lt;bean class=&quot;com.demo2.support.dao.impl.QueryDaoMybatisImpl&quot;&gt;

    &lt;property name=&quot;sqlMapper&quot; value=&quot;com.demo2.trade.query.dao.ProductMapper&quot;&gt;&lt;/property&gt;

   &lt;/bean&gt;

  &lt;/property&gt;

  &lt;property name=&quot;dao&quot; ref=&quot;basicDao&quot;&gt;&lt;/property&gt;

 &lt;/bean&gt;

&lt;/beans&gt;
</code></pre>
<p>在该案例中，productQry 本来应该配置 QueryServiceImpl，却替换为AutofillQueryServiceImpl。同时，在 vObj.xml 中进行了如下配置：</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;

&lt;vobjs&gt;

  &lt;vo class=&quot;com.demo2.trade.entity.Product&quot; tableName=&quot;Product&quot;&gt;

    &lt;property name=&quot;id&quot; column=&quot;id&quot; isPrimaryKey=&quot;true&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;name&quot; column=&quot;name&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;price&quot; column=&quot;price&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;unit&quot; column=&quot;unit&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;classify&quot; column=&quot;classify&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;supplier_id&quot; column=&quot;supplier_id&quot;&gt;&lt;/property&gt;

    &lt;join name=&quot;supplier&quot; joinKey=&quot;supplier_id&quot; joinType=&quot;manyToOne&quot; class=&quot;com.demo2.trade.entity.Supplier&quot;&gt;&lt;/join&gt;

  &lt;/vo&gt;

  &lt;vo class=&quot;com.demo2.trade.entity.Supplier&quot; tableName=&quot;Supplier&quot;&gt;

    &lt;property name=&quot;id&quot; column=&quot;id&quot; isPrimaryKey=&quot;true&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;name&quot; column=&quot;name&quot;&gt;&lt;/property&gt;

  &lt;/vo&gt;

&lt;/vobjs&gt;
</code></pre>
<p>在配置中可以看到，Product 的配置中增加了一个 join 标签，配置的是 Supplier，同时又配置了 Supplier 的查询。这样，当完成对 Product 的查询以后，发现有 join 标签，就会根据Supplier 的配置批量查询供应商，并自动补填到 Product 中。所以，只要有了这个 join，就必须要配置后面 Supplier，才能通过它查询数据库中的供应商数据，完成数据补填。</p>
<p>有了这样的设计，业务开发人员不必实现数据补填的烦琐代码，只需要在建模的时候配置好就可以了。要补填就配置 AutofillQueryServiceImpl，不补填就配置 QueryServiceImpl，整个系统就可以变得灵活而易于维护。特别需要注意的是，如果配置的是 AutofillQueryServiceImpl，那么除了配置 queryDao，还要配置 basicDao。因为在数据补填时，是通过 basicDao 采用 load() 或 loadForList() 进行补填的。</p>
<h3>数据补填对微服务的支持</h3>
<p>从以上案例可以看到，对 Product 补填 Supplier，这两个表的数据必须要在<strong>同一个数据库里</strong>，这在单体应用是 OK 的，但到微服务就不 OK 了。微服务不仅拆分了应用，还拆分了数据库。当 Product 微服务要补填 Supplier 时，是没有权限读取 Supplier 所在的数据库，只能远程调用 Supplier 微服务的相应接口。这样，通过以上配置完成数据补填就不行了，必须要<strong>技术中台</strong>提供对微服务的相应支持。</p>
<p>在微服务系统中，通过远程接口进行数据补填的需求，在基于 DDD 的设计开发中非常常见，因此技术中台必须针对这样的情况提供支持。为此，我在 join 标签的基础上又提供了 ref 标签。假设系统通过微服务的拆分，将 Product 与 Supplier 拆分到两个微服务中。这时，要在 Product 微服务中的 vObj.xml 文件中进行如下配置：</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;

&lt;vobjs&gt;

  &lt;vo class=&quot;com.demo2.product.entity.Product&quot; tableName=&quot;Product&quot;&gt;

    &lt;property name=&quot;id&quot; column=&quot;id&quot; isPrimaryKey=&quot;true&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;name&quot; column=&quot;name&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;price&quot; column=&quot;price&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;unit&quot; column=&quot;unit&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;classify&quot; column=&quot;classify&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;supplier_id&quot; column=&quot;supplier_id&quot;&gt;&lt;/property&gt;

    &lt;ref name=&quot;supplier&quot; refKey=&quot;supplier_id&quot; refType=&quot;manyToOne&quot; 

      bean=&quot;com.demo2.product.service.SupplierService&quot; method=&quot;loadSupplier&quot; listMethod=&quot;loadSuppliers&quot;&gt;

    &lt;/ref&gt;

  &lt;/vo&gt;

&lt;/vobjs&gt;
</code></pre>
<p>以上配置将 join 标签改为了 ref 标签。在 ref 标签中，bean 就是在 Product 微服务中对Supplier 微服务进行远程调用的 Feign 接口（详见第 15 讲）。这时，需要 Supplier 微服务提供 2 个查询接口：</p>
<ul>
<li>Supplier loadSupplier(id)，即通过某个 ID 进行查找；</li>
<li>List loadSupplier(Listids)，通过多个 ID 进行批量查找。</li>
</ul>
<p>在这里，<strong>method 配置的是对单个 ID 进行查找的方法</strong>，<strong>listMethod 配置的是对多个 ID 批量查找的方法</strong>。通过这 2 个配置，就可以用 Feign 接口实现微服务的远程调用，完成跨微服务的数据补填。通过这样的设计，在 Product 微服务的 vObj.xml 中就不用配置 Supplier 了。</p>
<h3>通用仓库与工厂的设计</h3>
<p>没有采用 DDD 之前，在系统的设计中，每个 Service 都是直接注入 Dao，通过 Dao 来完成业务对数据库的操作。然而，DDD 的架构设计增加了仓库与工厂，除了<strong>读写数据库</strong>以外，还要<strong>实现对领域对象的映射与装配</strong>。那么，DDD 的仓库与工厂，和以往的 Dao 是什么关系呢？又应当如何设计呢？</p>
<p>传统的 DDD 设计，每个模块都有自己的<strong>仓库与工厂</strong>，工厂是领域对象创建与装配的地方，是生命周期的开始。创建出来后放到仓库的缓存中，供上层应用访问。当领域对象在经过一系列操作以后，最后通过仓库完成数据的持久化。这个领域对象数据持久化的过程，对于普通领域对象来说就是存入某个单表，然而对于有聚合关系的领域对象来说，需要存入多个表中，并将其放到同一事务中。</p>
<p>在这个过程中，<strong>聚合关系会出现跨库的事务操作吗</strong>？即具有聚合关系的多个领域对象会被拆分为多个微服务吗？我认为是不可能的，因为聚合就是一种<strong>强相关的封装</strong>，是不可能因微服务而拆分的。如果出现了，要么不是聚合关系，要么就是微服务设计出现了问题。因此，仓库是不可能完成跨库的事务处理的。</p>
<p>弄清楚了传统的 DDD 设计，与以往 Dao 的设计进行比较，就会发现仓库和工厂就是对 Dao 的替换。然而，这种替换不是简单的替换，它们对 Dao 替换的同时，还<strong>扩展了许多的功能</strong>，如数据的补填、领域对象的映射与装配、聚合的处理，等等。当我们把这些关系思考清楚了，通用仓库与工厂的设计就出来了。</p>
<p><img src="assets/CgpVE1_4DGKAEhouAABuNiM-xKQ436.png" alt="Lark20210108-153942.png" /></p>
<p>如上图所示，仓库就是一个 Dao，它实现了 BasicDao 的接口。然而，仓库在读写数据库时，是把 BasicDao 实现类的代码重新 copy 一遍吗？不！那样只会形成大量重复代码，不利于日后的变更与维护。因此，仓库通过一个属性变量将 BasicDao 包在里面。这样，当仓库要读写数据库时，实际上调用的是 BasicDao 实现类，仓库仅仅实现在 BasicDao 实现类基础上扩展的那些功能。这样，仓库与 BasicDao 实现类彼此之间的职责与边界就划分清楚了。</p>
<p>有了这样的设计，原有的遗留系统要通过改造转型为 DDD，除了通过领域建模增加 vObj.xml以外，将原来注入 Dao 改为注入仓库，就可以快速完成领域驱动的转型。同样的道理，要在仓库中增加缓存的功能，不是直接去修改仓库，而是在仓库的基础上包一个RepositoryWithCache，专心实现缓存的功能。这样设计，既使各个类的职责划分非常清楚，日后因哪种缘由变更就改哪个类，又使得系统设计松耦合，可以通过组件装配满足各种需求。</p>
<h3>总结</h3>
<p>通过本讲的讲述，我为你提供了一个可以落地的技术中台。这个中台与传统的 DDD 架构有所不同，它摒弃了一些非常烦琐的 TDO、PO、仓库与工厂的设计，而是将其封装在了底层技术框架中。这样，业务开发人员可以将更多的精力放到业务建模，以及基于业务建模的设计开发过程中。开发工作量减少了，一方面可以实现<strong>快速交付</strong>，另一方面也让日后的<strong>变更与维护变得轻松</strong>，可以随着领域模型的变更而变更，更好更深刻地设计我们的产品，给用户更好的体验。</p>
<p>下一讲我们将围绕事件驱动，来谈一谈其在微服务中的设计实现。</p>
<p><a href="https://github.com/mooodo/demo-service2-support">点击 GitHub 链接</a>，查看源码。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="16&#32;&#32;基于&#32;DDD&#32;的代码设计演示（含&#32;DDD&#32;的技术中台设计）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="18&#32;&#32;基于事件溯源的设计开发.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433e49ec5770ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/DDD%20%E5%BE%AE%E6%9C%8D%E5%8A%A1%E8%90%BD%E5%9C%B0%E5%AE%9E%E6%88%98/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
