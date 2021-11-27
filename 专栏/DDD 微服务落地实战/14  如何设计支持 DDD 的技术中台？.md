<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>14  如何设计支持 DDD 的技术中台？.md</title>
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

                    <a class="current-tab" href="14&#32;&#32;如何设计支持&#32;DDD&#32;的技术中台？.md">14  如何设计支持 DDD 的技术中台？.md</a>
                    

                </li>
                <li>

                    
                    <a href="15&#32;&#32;如何设计支持微服务的技术中台？.md">15  如何设计支持微服务的技术中台？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;基于&#32;DDD&#32;的代码设计演示（含&#32;DDD&#32;的技术中台设计）.md">16  基于 DDD 的代码设计演示（含 DDD 的技术中台设计）.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;基于&#32;DDD&#32;的微服务设计演示（含支持微服务的&#32;DDD&#32;技术中台设计）.md">17  基于 DDD 的微服务设计演示（含支持微服务的 DDD 技术中台设计）.md</a>

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
                        <div><h1>14  如何设计支持 DDD 的技术中台？</h1>
<p>DDD 要落地实践，最大的“坑”就是支持 DDD 的技术架构如何设计。很多团队在工作开展前期，一切都很顺利：通过对业务需求的理解，建立领域模型；将领域模型通过一系列的设计，落实程序设计，准确地说是程序设计中业务领域层的设计。然而就在编码实现的时候，出现了各种问题：</p>
<ul>
<li>要么是不能准确掌握 DDD 的分层架构；</li>
<li>要么是把程序写得非常乱，频繁地在各种 TDO、DO、PO 之间进行数据转换，耗费大量代码，使得日后变更异常困难。</li>
</ul>
<p>因此，还需要有一个强有力的技术中台的支持，来简化 DDD 的设计实现，解决“最后一公里”的问题。唯有这样，DDD 才能在项目中真正落地。</p>
<h3>传统 DDD 的架构设计</h3>
<p><img src="assets/CgqCHl_q05-AX01vAAB19K5BZDQ843.png" alt="Drawing 1.png" /></p>
<p>通常，在支持领域驱动的软件项目中，架构设计如上图所示。</p>
<ul>
<li><strong>展现层</strong>是前端的 UI，它通过网络与后台的应用层交互。</li>
<li><strong>应用层</strong>类似于 MVC 层，主要用于前后端交互，在接收用户请求后，会去调用领域层的服务，也就是 Service。</li>
<li>在<strong>领域层</strong>中，用户请求首先由 Service 接收，然后在执行业务操作的过程中，使用领域对象作为参数（贫血模型的实现），或者去调用领域对象中的相应方法（充血模型的实现）。在领域对象的设计上，可以是实体，也可以是值对象，也可以将它们制作成一个聚合（如果多个领域对象间存在整体与部分的关系）。</li>
<li>最后，通过仓库将领域对象中的<strong>数据持久化到数据库</strong>；使用工厂将数据从数据库中<strong>读取</strong>、<strong>拼装</strong>并<strong>还原</strong>成领域对象。</li>
</ul>
<p>这些都是将领域驱动落地到软件设计时所采用的方式。从架构分层上说，DDD 的仓库和工厂的设计介于业务领域层与基础设施层之间，即接口在业务领域层，而实现在基础设施层。DDD 的基础设施层相当于支撑 DDD 的基础技术架构，通过各种技术框架支持软件系统完成除了领域驱动以外的各种功能。</p>
<p><img src="assets/Cip5yF_tSR6AMldHAAElu3pD1us550.png" alt="1.png" /></p>
<p>然而，传统的软件系统采用 DDD 进行架构设计时，需要在各个层次之间进行各种数据结构的转换：</p>
<ul>
<li>首先，前端的数据结构是 JSON，传递到后台数据接入层时需要将其转换为数据传输对象DTO；</li>
<li>然后应用层去调用领域层时，需要将 DTO 转换为领域对象 DO；</li>
<li>最后，将数据持久化到数据库时，又要将 DO 转换为持久化对象 PO。</li>
</ul>
<p>在这个过程中，需要编写大量代码进行<strong>数据的转换</strong>，无疑将加大软件开发的工作量与日后变更的维护成本。因此，我们可不可以考虑上一讲所提到的设计，将各个层次的数据结构统一起来呢？</p>
<p><img src="assets/Ciqc1F_q07uAXmqhAAERd9ZE2WA787.png" alt="Drawing 5.png" /></p>
<p>另外，传统的软件系统在采用 DDD 进行架构设计时，需要为每一个功能模块编写各自的仓库与工厂，如订单模块有订单仓库与订单工厂、库存模块有库存仓库与库存工厂。各个模块在编写仓库与工厂时，虽然实现了各自不同的业务，却形成了<strong>大量重复的代码</strong>。这样的问题与前面探讨的 Dao 的问题一样，是否可以通过配置与建模，设计成一个统一的仓库与工厂。如果是这样，那么仓库与工厂又与 Dao 是什么关系呢？基于对以上问题的思考，我提出了统一数据建模、内置聚合的实现、通用仓库和工厂，来简化 DDD 业务开发。因此，进行了如下的架构设计。</p>
<h3>通用仓库与通用工厂的设计</h3>
<p><img src="assets/CgqCHl_q08eAJ2WOAAIrg-1_zI4002.png" alt="Drawing 7.png" /></p>
<p>该设计与上一讲的架构设计相比，差别仅是将单 Dao 替换为了通用仓库与通用工厂。也就是说，与 Dao 相比，DDD 的仓库就是在 Dao 的基础上<strong>扩展了一些新的功能</strong>。</p>
<ul>
<li>例如在<strong>装载或查询订单</strong>时，不仅要查询订单表，还要补填与订单相关的订单明细与客户信息、商品信息，并装配成一个订单对象。在这个过程中，查询订单是 Dao 的功能，但其他类似补填、装配等操作，则是仓库在 Dao 基础上进行的功能扩展。</li>
<li>同样，在<strong>保存订单</strong>时，不仅要保存订单表，还要保存订单明细表，并将它们放到同一个事务中。保存订单表是 Dao 原有的功能，保存订单明细表并添加事务，则是仓库在 Dao 基础上进行的功能扩展。</li>
</ul>
<p>这就是 DDD 的仓库与 Dao 的关系。</p>
<p>基于这种扩展关系，该如何设计这个通用仓库呢？如果熟悉设计模式，则会想到“装饰者模式”。“装饰者模式”的目的，就是在原有功能的基础上进行“透明功能扩展”。这种“透明功能扩展”，既可以扩展原有功能，又不影响原有的客户程序，使客户程序不用修改任何代码就能实现新功能，从而降低变更的维护成本。因此，将“通用仓库”设计成了这样。</p>
<p><img src="assets/CgqCHl_q08-AagbGAAA1dTvg3n0066.png" alt="Drawing 9.png" /></p>
<p>即在原有的 BasicDao 与 BasicDaoImpl 的基础上，增加了通用仓库 Repository。将 Repository 设计成装饰者，它也是接口 BasicDao 的实现类，是通过一个属性变量引用的 BasicDao。使用时，在 BasicDaoImpl 的基础上包一个 Repository，就可以扩展出那些 DDD 的功能。因此，所有的 Service 在注入 Dao 的时候：</p>
<ul>
<li>如果不使用 DDD，则像以前一样注入BasicDaoImpl；</li>
<li>如果需要使用 DDD，则注入 Repository。</li>
</ul>
<p>配置如下：</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;

&lt;beans xmlns=&quot;http://www.springframework.org/schema/beans&quot; ...&gt;

 &lt;description&gt;The application context for orm&lt;/description&gt;

 &lt;bean id=&quot;basicDao&quot; class=&quot;com...impl.BasicDaoJdbcImpl&quot;&gt;&lt;/bean&gt;

 &lt;bean id=&quot;redisCache&quot; class=&quot;com...cache.RedisCache&quot;&gt;&lt;/bean&gt;

 &lt;bean id=&quot;repository&quot; class=&quot;com...RepositoryWithCache&quot;&gt;

  &lt;property name=&quot;dao&quot; ref=&quot;basicDao&quot;&gt;&lt;/property&gt;

  &lt;property name=&quot;cache&quot; ref=&quot;redisCache&quot;&gt;&lt;/property&gt;

 &lt;/bean&gt;

 &lt;bean id=&quot;product&quot; class=&quot;com.demo2...impl.ProductServiceImpl&quot;&gt;

  &lt;property name=&quot;dao&quot; ref=&quot;repository&quot;&gt;&lt;/property&gt;

 &lt;/bean&gt;

 &lt;bean id=&quot;supplier&quot; class=&quot;com.demo2...impl.SupplierServiceImpl&quot;&gt;

  &lt;property name=&quot;dao&quot; ref=&quot;basicDao&quot;&gt;&lt;/property&gt;

 &lt;/bean&gt;

 &lt;bean id=&quot;productQry&quot; class=&quot;com.demo2...AutofillQueryServiceImpl&quot;&gt;

  &lt;property name=&quot;queryDao&quot;&gt;

   &lt;bean class=&quot;com.demo2.support.dao.impl.QueryDaoMybatisImpl&quot;&gt;

    &lt;property name=&quot;sqlMapper&quot; value=&quot;com.demo2...dao.ProductMapper.query&quot;&gt;&lt;/property&gt;

   &lt;/bean&gt;

  &lt;/property&gt;

  &lt;property name=&quot;dao&quot; ref=&quot;basicDao&quot;&gt;&lt;/property&gt;

 &lt;/bean&gt;

&lt;/beans&gt;
</code></pre>
<p>在这一配置中可以看到，Repository 中有一个属性 Dao 配置的是 BasicDao。这样当 Repository 访问数据库时，通过 BasicDao 进行访问。同时，这里实现了两个通用仓库：Repository 与 RepositoryWithCache。如果配置后者则可以实现缓存的功能。</p>
<p>在以上示例中，Product 将 Dao 配置为 Repository。这样，Product 在通过 ID 装载时，就会在产品对象中加载与其关联的供应商 Supplier。同时，productQry 将 queryDao 配置为 AutofillQueryServiceImpl，则在查询产品信息以后，会自动补填与其关联的供应商 Supplier。</p>
<p>这里，通用仓库是如何指导 Product 关联 Supplier 的呢？关键就在于文件 vObj.xml 进行了以下配置：</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;

&lt;vobjs&gt;

  &lt;vo class=&quot;com.demo2.trade.entity.Product&quot; tableName=&quot;Product&quot;&gt;

    &lt;property name=&quot;id&quot; column=&quot;id&quot; isPrimaryKey=&quot;true&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;name&quot; column=&quot;name&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;price&quot; column=&quot;price&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;unit&quot; column=&quot;unit&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;classify&quot; column=&quot;classify&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;supplier_id&quot; column=&quot;supplier_id&quot;&gt;&lt;/property&gt;

    &lt;join name=&quot;supplier&quot; joinKey=&quot;supplier_id&quot; joinType=&quot;manyToOne&quot;       class=&quot;com.demo2.trade.entity.Supplier&quot;&gt;&lt;/join&gt;

  &lt;/vo&gt;

  &lt;vo class=&quot;com.demo2.trade.entity.Supplier&quot; tableName=&quot;Supplier&quot;&gt;

    &lt;property name=&quot;id&quot; column=&quot;id&quot; isPrimaryKey=&quot;true&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;name&quot; column=&quot;name&quot;&gt;&lt;/property&gt;

  &lt;/vo&gt;

&lt;/vobjs&gt;
</code></pre>
<p>在 Product 中增加了<strong>join 标签</strong>，<strong>标注领域对象间的关联关系</strong>。其中 joinKey=“supplier_id”，代表在 Product 对象中的属性 supplier_id 用于与 Supplier 的 key 值关联。joinType 代表关联类型，支持 oneToOne、manyToOne、oneToMany 三种类型的关联，但基于性能的考虑，不支持 manyToMany。当类型是 oneToMany 时，补填的是一个集合，因此领域对象中也应当是一个集合属性，例如 Customer 中有一个 Address 是 oneToMany，因此领域对象设计成这样：</p>
<pre><code>/**

 * The customer entity

 * @author fangang

 */

public class Customer extends Entity&lt;Long&gt; {

 ......

 private List&lt;Address&gt; addresses;

 /**

  * @return the addresses

  */

 public List&lt;Address&gt; getAddresses() {

  return addresses;

 }

 /**

  * @param addresses the addresses to set

  */

 public void setAddresses(List&lt;Address&gt; addresses) {

  this.addresses = addresses;

 }

}
</code></pre>
<p>因此，在 vObj.xml 中进行如下配置：</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;

&lt;vobjs&gt;

  &lt;vo class=&quot;com.demo2.customer.entity.Customer&quot; tableName=&quot;Customer&quot;&gt;

    &lt;property name=&quot;id&quot; column=&quot;id&quot; isPrimaryKey=&quot;true&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;name&quot; column=&quot;name&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;sex&quot; column=&quot;sex&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;birthday&quot; column=&quot;birthday&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;identification&quot; column=&quot;identification&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;phone_number&quot; column=&quot;phone_number&quot;&gt;&lt;/property&gt;

    &lt;join name=&quot;addresses&quot; joinKey=&quot;customer_id&quot; joinType=&quot;oneToMany&quot; isAggregation=&quot;true&quot; class=&quot;com.demo2.customer.entity.Address&quot;&gt;&lt;/join&gt;

  &lt;/vo&gt;

  &lt;vo class=&quot;com.demo2.customer.entity.Address&quot; tableName=&quot;Address&quot;&gt;

   &lt;property name=&quot;id&quot; column=&quot;id&quot; isPrimaryKey=&quot;true&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;customer_id&quot; column=&quot;customer_id&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;country&quot; column=&quot;country&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;province&quot; column=&quot;province&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;city&quot; column=&quot;city&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;zone&quot; column=&quot;zone&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;address&quot; column=&quot;address&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;phone_number&quot; column=&quot;phone_number&quot;&gt;&lt;/property&gt;

  &lt;/vo&gt;

&lt;/vobjs&gt;
</code></pre>
<p>这样，在装载和查询 Customer 时，内置就将它关联的 Address 也加载出来了。在加载中，通过 Dao 去数据库中查询数据，然后将查询到的 Customer 与多个 Address 交给通用工厂去装配。如果配置的是 RepositoryWithCache，则加载 Customer 时会先检查缓存中有没有该客户。如果没有则到数据库中查询。</p>
<h3><strong>内置聚合功能</strong></h3>
<p><strong>聚合</strong>是领域驱动设计中一个非常重要的概念，它代表在真实世界中的整体与部分的关系。比如，Order（订单）与 OrderItem（订单明细）就是一个整体与部分的关系。当加载一个订单时，应当同时加载其订单明细，而保存订单时应当同时保存订单与订单明细，并放在同一事务中。在设计支持领域驱动的技术中台时，应当简化聚合的设计与实现，让业务开发人员不必每次都编写大量代码，而是通过一个配置就可以完成聚合的实现。</p>
<p>例如，订单与订单明细存在聚合关系，则在 vObj.xml 中建模时，通过 join 标签关联它们，并置 join 标签的 isAggregation=true。这样，在查询或装载订单的同时，装载它的所有订单明细，而在保存订单时保存订单明细，并将它们置于同一事务中。具体配置如下：</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;

&lt;vobjs&gt;

  &lt;vo class=&quot;com.demo2.order.entity.Customer&quot; tableName=&quot;Customer&quot;&gt;

    &lt;property name=&quot;id&quot; column=&quot;id&quot; isPrimaryKey=&quot;true&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;name&quot; column=&quot;name&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;sex&quot; column=&quot;sex&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;birthday&quot; column=&quot;birthday&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;identification&quot; column=&quot;identification&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;phone_number&quot; column=&quot;phone_number&quot;&gt;&lt;/property&gt;

    &lt;join name=&quot;addresses&quot; joinKey=&quot;customer_id&quot; joinType=&quot;oneToMany&quot; isAggregation=&quot;true&quot; class=&quot;com.demo2.order.entity.Address&quot;&gt;&lt;/join&gt;

  &lt;/vo&gt;

  &lt;vo class=&quot;com.demo2.order.entity.Address&quot; tableName=&quot;Address&quot;&gt;

   &lt;property name=&quot;id&quot; column=&quot;id&quot; isPrimaryKey=&quot;true&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;customer_id&quot; column=&quot;customer_id&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;country&quot; column=&quot;country&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;province&quot; column=&quot;province&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;city&quot; column=&quot;city&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;zone&quot; column=&quot;zone&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;address&quot; column=&quot;address&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;phone_number&quot; column=&quot;phone_number&quot;&gt;&lt;/property&gt;

  &lt;/vo&gt;

  &lt;vo class=&quot;com.demo2.order.entity.Product&quot; tableName=&quot;Product&quot;&gt;

    &lt;property name=&quot;id&quot; column=&quot;id&quot; isPrimaryKey=&quot;true&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;name&quot; column=&quot;name&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;price&quot; column=&quot;price&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;unit&quot; column=&quot;unit&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;classify&quot; column=&quot;classify&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;supplier_id&quot; column=&quot;supplier_id&quot;&gt;&lt;/property&gt;

  &lt;/vo&gt;

  &lt;vo class=&quot;com.demo2.order.entity.Order&quot; tableName=&quot;Order&quot;&gt;

   &lt;property name=&quot;id&quot; column=&quot;id&quot; isPrimaryKey=&quot;true&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;customer_id&quot; column=&quot;customer_id&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;address_id&quot; column=&quot;address_id&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;amount&quot; column=&quot;amount&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;order_time&quot; column=&quot;order_time&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;flag&quot; column=&quot;flag&quot;&gt;&lt;/property&gt;

   &lt;join name=&quot;customer&quot; joinKey=&quot;customer_id&quot; joinType=&quot;manyToOne&quot; class=&quot;com.demo2.order.entity.Customer&quot;&gt;&lt;/join&gt;

   &lt;join name=&quot;address&quot; joinKey=&quot;address_id&quot; joinType=&quot;manyToOne&quot; class=&quot;com.demo2.order.entity.Address&quot;&gt;&lt;/join&gt;

   &lt;join name=&quot;orderItems&quot; joinKey=&quot;order_id&quot; joinType=&quot;oneToMany&quot; isAggregation=&quot;true&quot; class=&quot;com.demo2.order.entity.OrderItem&quot;&gt;&lt;/join&gt;

  &lt;/vo&gt;

  &lt;vo class=&quot;com.demo2.order.entity.OrderItem&quot; tableName=&quot;OrderItem&quot;&gt;

   &lt;property name=&quot;id&quot; column=&quot;id&quot; isPrimaryKey=&quot;true&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;order_id&quot; column=&quot;order_id&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;product_id&quot; column=&quot;product_id&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;quantity&quot; column=&quot;quantity&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;price&quot; column=&quot;price&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;amount&quot; column=&quot;amount&quot;&gt;&lt;/property&gt;

   &lt;join name=&quot;product&quot; joinKey=&quot;product_id&quot; joinType=&quot;manyToOne&quot; class=&quot;com.demo2.order.entity.Product&quot;&gt;&lt;/join&gt;

  &lt;/vo&gt;

&lt;/vobjs&gt;
</code></pre>
<p>在该配置中可以看到，订单不仅与订单明细关联，还与客户、客户地址等信息关联。但是，订单与客户、客户地址等信息不存在聚合关系，当保存订单时不需要保存或更改这些信息。只有订单明细与订单具有聚合关系，在订单中配置订单明细的 join 标签时，才需要增加isAggregation=true。这样，当保存订单时，同时也保存订单明细，并将它们放到同一事务中。通过这样的设计，既<strong>简化了聚合的实现</strong>，又使得<strong>聚合实现在底层技术中台中</strong>，与业务代码无关。因此，系统可以通过底层不断优化对聚合的设计实现，使变更成本更低。</p>
<h3>总结</h3>
<p>本讲通过一个支持 DDD 的技术中台，将许多 DDD 繁杂的设计实现，做成通用的仓库与工厂，封装在了底层的技术中台中。这样，业务开发人员就可以更加专注于领域建模，将模型按照一定的规范进行配置，来完成基于 DDD 的设计开发。而底层的技术中台就可以根据这些配置，完成相应的数据持久化与查询装载了。</p>
<p>同时，以上设计简化了系统设计，不再需要将数据在 JSON、TDO、DO、PO 中进行转换，而是通过规范，将 JSON 与 DO 设计一致，将 DO 与数据库进行配置，就可以完成开发。代码减少了，日后的维护与变更也变得容易了。</p>
<p>另外，有同学问了一个有趣的问题：我在查询订单的时候本来不想加载订单明细，而加载了订单明细，是不是会影响性能。答案是肯定的，所以说未来在面对高并发时，应当采用富客户端以减少前后交互次数。因此，在设计上应当尽量多加载一些数据到前端，使更多操作直接在前端进行。这样就有效减少了交互次数，降低了系统压力。</p>
<p>下一讲将进一步探讨支持 DDD 的微服务，技术中台该如何设计。</p>
<p><a href="https://github.com/mooodo/demo-service2-support">点击 GitHub 链接</a>，查看源码。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="13&#32;&#32;如何实现支持快速交付的技术中台设计？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="15&#32;&#32;如何设计支持微服务的技术中台？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433e37b87e70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
