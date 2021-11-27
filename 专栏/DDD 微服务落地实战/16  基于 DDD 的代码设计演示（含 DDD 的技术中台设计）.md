<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>16  基于 DDD 的代码设计演示（含 DDD 的技术中台设计）.md</title>
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

                    <a class="current-tab" href="16&#32;&#32;基于&#32;DDD&#32;的代码设计演示（含&#32;DDD&#32;的技术中台设计）.md">16  基于 DDD 的代码设计演示（含 DDD 的技术中台设计）.md</a>
                    

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
                        <div><h1>16  基于 DDD 的代码设计演示（含 DDD 的技术中台设计）</h1>
<p>我这些年的从业经历，起初是作为项目经理带团队做软件研发，后来转型成为架构师，站在更高的层面去思考软件研发的那些事儿。我认为，一个成熟的软件研发团队：</p>
<ul>
<li>不仅在于团队成员<strong>研发水平</strong>的提高；</li>
<li>更在于将不断积累的通用的<strong>设计方法</strong>与<strong>技术框架</strong>，沉淀到底层的技术中台中。</li>
</ul>
<p>只要有了这样的技术中台作为支撑，才能让研发团队具备更强的能力，用更快的速度，研发出更多的产业，以快速适应激烈竞争而快速变化的市场。</p>
<p>譬如，团队某次接到了一个<strong>数据推送</strong>的需求，在完成了该需求并交付用户以后，就在这个功能设计的基础上，抽取共性、保留个性，将其下沉到技术中台形成“数据共享平台”的设计。有了这个功能，团队日后在接到类似需求时，只需要进行一些配置或者简单开发，就能交付用户啦。</p>
<p>这样，团队的研发能力就大大提升了。团队研发的功能越多，沉淀到技术中台的功能就越多，团队研发能力的提升就越大。只有这样的技术中台才能支撑研发团队的快速交付，关键是要有人、有意识地去做这些工作的整理，而我们团队是在“使能故事”中完成这些工作的。</p>
<p>现如今，越来越多的团队采用敏捷开发，在 2~3 周的迭代周期中规划并完成“用户故事”。“用户故事”是需要紧急应对的用户需求，但如果不能提升团队的能力，那么团队就会像救火队员一样永远是在应对用户需求的“火”而疲于奔命。</p>
<p>相反，“使能故事（Enabler Story）”就是为了提升我们的能力，从而更快速地应对用户需求。俗话说：“磨刀不误砍柴工”，“使能故事”就是“磨刀”，它虽然要耗费一些时间，但可以让日后的“砍柴”更快更好，是很值得的。</p>
<p>因此，一个成熟的团队在每次的迭代中不能只是完成“用户故事”，而应该拿出一定比例的时间完成“使能故事”，使团队日后的“用户故事”做得更快，实现快速交付。</p>
<p>我的支持 DDD + 微服务的技术中台就是在这种指导下逐渐形成的。之前在我的团队实践 DDD + 微服务的过程中，遇到了很多的阻力。这种阻力要求团队成员花更多的时间学习 DDD 相关知识，用正确的方法与步骤去设计开发，并做到位。然而，当他们真正做到位以后，却发现 DDD 的设计开发非常烦琐，要频繁地实现各种工厂、仓库、数据补填等开发工作，使开发人员对 DDD 的开发心生厌恶。以往项目经理在面对这些问题时，只能从管理上制定开发规范，但这样的措施于事无补。</p>
<p>而我站在架构师的角度，去设计技术框架，在原有代码的基础上，抽取共性、保留个性，将烦琐的 DDD 开发封装在了技术中台中。这样做，不仅简化了设计开发，使得 DDD 更容易在项目中落地，还规范了代码，使得业务开发人员没有机会去编写 Controller 与 Dao 代码，自然而然地将业务代码基于领域模型设计在了 Service 与领域对象中了。接着，来看看这个框架的设计。</p>
<h3>整个演示代码的架构</h3>
<p>我把整个演示代码分享在了 <a href="https://github.com/mooodo">GitHub</a> 中，它分为这样几个项目。</p>
<ul>
<li>demo-ddd-trade：一个基于 DDD 设计的单体应用。</li>
<li>demo-parent：本示例所有微服务项目的父项目。</li>
<li>demo-service-eureka：微服务注册中心 eureka。</li>
<li>demo-service-config：微服务配置中心 config。</li>
<li>demo-service-turbine：各微服务断路器监控 turbine。</li>
<li>demo-service-zuul：服务网关 zuul。</li>
<li>demo-service-parent：各业务微服务（无数据库访问）的父项目。</li>
<li>demo-service-support：各业务微服务（无数据库访问）底层技术框架。</li>
<li>demo-service-customer：用户管理微服务（无数据库访问）。</li>
<li>demo-service-product：产品管理微服务（无数据库访问）。</li>
<li>demo-service-supplier：供应商管理微服务（无数据库访问）。</li>
<li>demo-service2-parent：各业务微服务（有数据库访问）的父项目。</li>
<li>demo-service2-support：各业务微服务（有数据库访问）底层技术框架。</li>
<li>demo-service2-customer：用户管理微服务（有数据库访问）。</li>
<li>demo-service2-product：产品管理微服务（有数据库访问）。</li>
<li>demo-service2-supplier：供应商管理微服务（有数据库访问）。</li>
<li>demo-service2-order：订单管理微服务（有数据库访问）。</li>
</ul>
<p>总之，这里有一个基于 DDD 的单体应用与一个完整的微服务应用。在微服务应用中：</p>
<ul>
<li>demo-service-xxx 是我基于一个早期的框架设计的，你可以看到我们以往设计开发的原始状态；</li>
<li>而 demo-service2-xxx 是我需要重点讲解的基于 DDD 的微服务设计。</li>
</ul>
<p>其中，demo-service2-support 是这个框架的核心，即底层技术中台，而其他都是演示对它的具体应用。</p>
<h3>单 Controller 的设计实现</h3>
<p>与以往不同，在整个系统中只有几个 Controller，并下沉到了底层技术中台 demo-service2-support 中，它们包括以下几部分。</p>
<ul>
<li>OrmController：用于增删改操作，以及基于 key 值的 load、get 操作，它们通常基于DDD 进行设计。</li>
<li>QueryController：用于基于 SQL 语句形成的查询分析报表，它们通常不基于 DDD 进行设计，但查询结果会形成领域对象，并基于 DDD 进行数据补填。</li>
<li>其他 Controller，用于如 ExcelController 等特殊的操作，是继承以上两个类的功能扩展。</li>
</ul>
<p>OrmController 接收诸如 orm/{bean}/{method} 的请求，bean 是配置在 Spring 中的 bean，method 是 bean 中要调用的方法。由于这是一个基础框架，没有限定前端可以调用哪些方法，因此实际项目需要在此之上增加权限校验。该方法既可以接收 GET 方法，也可以接收 POST 方法，因此其他的参数可以根据 GET/POST 各自的方式进行传递。</p>
<p>这里的 bean 对应的是后台的 Service。Service 的编写要求所有的方法，如果需要使用领域对象必须放在第一个参数上。如果第一个参数是简单的数字、字符串、日期等类型，就不是领域对象，否则就作为领域对象，依次从前端上传的 JSON 中获取相应的数据予以填充。这里暂时不支持集合，也不支持具有继承关系的领域对象，待我日后完善。判定代码如下：</p>
<pre><code> /**

  * check a parameter whether is a value object.

  * @param clazz

  * @return yes or no

  * @throws IllegalAccessException 

  * @throws InstantiationException 

  */

 private boolean isValueObject(Class&lt;?&gt; clazz) {

  if(clazz==null) return false;

  if(clazz.equals(long.class)||clazz.equals(int.class)||

    clazz.equals(double.class)||clazz.equals(float.class)||

    clazz.equals(short.class)) return false;

  if(clazz.isInterface()) return false;

  if(Number.class.isAssignableFrom(clazz)) return false;

  if(String.class.isAssignableFrom(clazz)) return false;

  if(Date.class.isAssignableFrom(clazz)) return false;

  if(Collection.class.isAssignableFrom(clazz)) return false;

  return true;

 }
</code></pre>
<p>这里的开发规范除了要求 Service 的所有方法中的领域对象放第一个参数，还要求前端的 JSON 与领域对象中的属性一致，这样才能完成自动转换，而不需要为每个模块编写 Controller。</p>
<p>QueryController 接收诸如 query/{bean} 的请求，这里的 bean 依然是 Spring 中配置的bean。同样，该方法也是既可以接收 GET 方法，也可以接收 POST 方法，并用各自的方式传递查询所需的参数。</p>
<p>如果该查询需要分页，那么在传递查询参数以外，还要传递 page（第几页）与 size（每页多少条记录）。第一次查询时，除了分页，还会计算 count 并返回前端。这样，在下次分页查询时，将 count 也作为参数传递，将不再计算 count，从而提升查询效率。此外，这里还将提供求和功能，敬请期待。</p>
<h3>单 Dao 的设计实现</h3>
<p>以往系统设计的硬伤在于一头一尾：Controller 与 Dao。它既要为每个模块编写大量代码，也使得系统设计非常不 DDD，令日后的变更维护成本巨大。因此，我在大量系统设计问题分析的基础上，提出了单 Controller 与单 Dao 的设计思路。前面讲解了单 Controller 的设计，现在来看一看单 Dao 的设计。</p>
<p>诚然，当今的主流是使用注解。然而，注解的使用存在诸多的问题。</p>
<ul>
<li>首先，它会带来业务代码与技术框架的依赖，因此当在 Service 中加入注解时，就不得不与 Spring、Springcloud 耦合，使得日后转型其他技术框架困难重重。</li>
<li>此外，注解往往适用于一对一、多对一的场景，而一对多、多对多的场景往往非常麻烦。而本框架存在大量一对多、多对多的场景，因此我建议你还是回归到 XML 的配置方式。</li>
</ul>
<p>在项目中的所有 Service 都要有一个 BasicDao 的属性变量，例如：</p>
<pre><code>public class CustomerServiceImpl implements CustomerService {

 private BasicDao dao;

 /**

  * @return the dao

  */

 public BasicDao getDao() {

  return dao;

 }

 /**

  * @param dao the dao to set

  */

 public void setDao(BasicDao dao) {

  this.dao = dao;

 }

    ...

}
</code></pre>
<p>接着，在 applicationContext-orm.xml 中，配置业务操作的 Service：</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;

&lt;beans xmlns=&quot;http://www.springframework.org/schema/beans&quot; ...&gt;

 &lt;description&gt;The application context for orm&lt;/description&gt;

 &lt;bean id=&quot;customer&quot; class=&quot;com.demo2.trade.service.impl.CustomerServiceImpl&quot;&gt;

  &lt;property name=&quot;dao&quot; ref=&quot;repositoryWithCache&quot;&gt;&lt;/property&gt;

 &lt;/bean&gt;

 &lt;bean id=&quot;product&quot; class=&quot;com.demo2.trade.service.impl.ProductServiceImpl&quot;&gt;

  &lt;property name=&quot;dao&quot; ref=&quot;repositoryWithCache&quot;&gt;&lt;/property&gt;

 &lt;/bean&gt;

 &lt;bean id=&quot;supplier&quot; class=&quot;com.demo2.trade.service.impl.SupplierServiceImpl&quot;&gt;

  &lt;property name=&quot;dao&quot; ref=&quot;basicDao&quot;&gt;&lt;/property&gt;

 &lt;/bean&gt;

 &lt;bean id=&quot;order&quot; class=&quot;com.demo2.trade.service.impl.OrderServiceImpl&quot;&gt;

  &lt;property name=&quot;dao&quot; ref=&quot;repository&quot;&gt;&lt;/property&gt;

 &lt;/bean&gt;

&lt;/beans&gt;
</code></pre>
<p>这里可以看到，每个 Service 都要注入 Dao，但可以根据需求注入不同的 Dao。</p>
<ul>
<li>如果该 Service 是纯贫血模型，那么注入 BasicDao 就可以了。</li>
<li>如果采用了充血模型，包含了一些聚合的操作，那么注入 repository 从而实现仓库与工厂的功能。</li>
<li>但如果还希望该仓库与工厂能提供缓存的功能，那么就注入 repositoryWithCache。</li>
</ul>
<p>例如，在以上案例中：</p>
<ul>
<li>SupplierService 实现的是非常简单的功能，注入 BasicDao 就可以了；</li>
<li>OrderService 实现了订单与明细的聚合，但数据量大不适合使用缓存，所以注入 repository；</li>
<li>CustomerService 实现了用户与地址的聚合，并且需要缓存，所以注入 repositoryWithCache；</li>
<li>ProductService 虽然没有聚合，但在查询产品时需要补填供应商，因此也注入repositoryWithCache。</li>
</ul>
<p>这里需要注意，是否使用缓存，也可以在日后的运维过程中，让运维人员通过修改配置去决定，从而提高系统的可维护性。</p>
<p>完成配置以后，核心是<strong>将领域建模映射成程序设计的模型</strong>。开发人员首先编写各个领域对象。譬如，产品要关联供应商，那么在增加 supplier_id 的同时，还要增加一个 Supplier 的属性：</p>
<pre><code>public class Product extends Entity&lt;Long&gt; {

 private static final long serialVersionUID = 7149822235159719740L;

 private Long id;

 private String name;

 private Double price;

 private String unit;

 private Long supplier_id;

 private String classify;

 private Supplier supplier;

    ...

}
</code></pre>
<p>注意，在本框架中的每个领域对象都必须要实现 Entity 这个接口，系统才知道你的主键是哪个。</p>
<p>接着，配置 vObj.xml，将领域对象与数据库对应起来：</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;

&lt;vobjs&gt;

  &lt;vo class=&quot;com.demo2.trade.entity.Customer&quot; tableName=&quot;Customer&quot;&gt;

    &lt;property name=&quot;id&quot; column=&quot;id&quot; isPrimaryKey=&quot;true&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;name&quot; column=&quot;name&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;sex&quot; column=&quot;sex&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;birthday&quot; column=&quot;birthday&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;identification&quot; column=&quot;identification&quot;&gt;&lt;/property&gt;

    &lt;property name=&quot;phone_number&quot; column=&quot;phone_number&quot;&gt;&lt;/property&gt;

    &lt;join name=&quot;addresses&quot; joinKey=&quot;customer_id&quot; joinType=&quot;oneToMany&quot; isAggregation=&quot;true&quot; class=&quot;com.demo2.trade.entity.Address&quot;&gt;&lt;/join&gt;

  &lt;/vo&gt;

  &lt;vo class=&quot;com.demo2.trade.entity.Address&quot; tableName=&quot;Address&quot;&gt;

   &lt;property name=&quot;id&quot; column=&quot;id&quot; isPrimaryKey=&quot;true&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;customer_id&quot; column=&quot;customer_id&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;country&quot; column=&quot;country&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;province&quot; column=&quot;province&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;city&quot; column=&quot;city&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;zone&quot; column=&quot;zone&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;address&quot; column=&quot;address&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;phone_number&quot; column=&quot;phone_number&quot;&gt;&lt;/property&gt;

  &lt;/vo&gt;

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

  &lt;vo class=&quot;com.demo2.trade.entity.Order&quot; tableName=&quot;Order&quot;&gt;

   &lt;property name=&quot;id&quot; column=&quot;id&quot; isPrimaryKey=&quot;true&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;customer_id&quot; column=&quot;customer_id&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;address_id&quot; column=&quot;address_id&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;amount&quot; column=&quot;amount&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;order_time&quot; column=&quot;order_time&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;flag&quot; column=&quot;flag&quot;&gt;&lt;/property&gt;

   &lt;join name=&quot;customer&quot; joinKey=&quot;customer_id&quot; joinType=&quot;manyToOne&quot; class=&quot;com.demo2.trade.entity.Customer&quot;&gt;&lt;/join&gt;

   &lt;join name=&quot;address&quot; joinKey=&quot;address_id&quot; joinType=&quot;manyToOne&quot; class=&quot;com.demo2.trade.entity.Address&quot;&gt;&lt;/join&gt;

   &lt;join name=&quot;orderItems&quot; joinKey=&quot;order_id&quot; joinType=&quot;oneToMany&quot; isAggregation=&quot;true&quot; class=&quot;com.demo2.trade.entity.OrderItem&quot;&gt;&lt;/join&gt;

  &lt;/vo&gt;

  &lt;vo class=&quot;com.demo2.trade.entity.OrderItem&quot; tableName=&quot;OrderItem&quot;&gt;

   &lt;property name=&quot;id&quot; column=&quot;id&quot; isPrimaryKey=&quot;true&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;order_id&quot; column=&quot;order_id&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;product_id&quot; column=&quot;product_id&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;quantity&quot; column=&quot;quantity&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;price&quot; column=&quot;price&quot;&gt;&lt;/property&gt;

   &lt;property name=&quot;amount&quot; column=&quot;amount&quot;&gt;&lt;/property&gt;

   &lt;join name=&quot;product&quot; joinKey=&quot;product_id&quot; joinType=&quot;manyToOne&quot; class=&quot;com.demo2.trade.entity.Product&quot;&gt;&lt;/join&gt;

  &lt;/vo&gt;

&lt;/vobjs&gt;
</code></pre>
<p>注意，在这里，所有用到 join 或 ref 标签的领域对象，其 Service 都必须使用 repository 或repositoryWithCache，以实现数据的自动补填，或者有聚合的地方实现聚合的操作，而注入 BasicDao 是无法实现这些操作的。</p>
<p>此外，各属性中的 name 配置的是该领域对象私有属性变量的名字，而不是 GET 方法的名字。例如，OrderItem 中配置的是 product_id，而不是 productId，并且该名字必须与数据库字段一致（这是 MyBatis 的要求，我也很无奈）。</p>
<p>有了以上的配置，就可以轻松实现 Service 对数据库的操作，以及 DDD 中那些烦琐的缓存、仓库、工厂、聚合、补填等操作。通过底层技术中台的封装，上层业务开发人员就可以专注于业务理解、领域建模，以及基于领域模型的业务开发，让 DDD 能更好、更快、风险更低地落地到实际项目中。</p>
<h3>总结</h3>
<p>本讲为你讲解了我设计的支持 DDD 的技术中台的设计开发思路，包括如何设计单 Controller、如何设计单 Dao，以及它们在项目中的应用。</p>
<p>下一讲我将更进一步讲解该框架如何设计单 Service 进行查询、通用仓库与通用工厂的设计，以及它们对微服务架构的支持。</p>
<p><a href="https://github.com/mooodo/demo-service2-support">点击 GitHub 链接</a>，查看源码。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="15&#32;&#32;如何设计支持微服务的技术中台？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="17&#32;&#32;基于&#32;DDD&#32;的微服务设计演示（含支持微服务的&#32;DDD&#32;技术中台设计）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433e4579ec70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
