<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>20  服务监控：如何使用 Actuator 组件实现系统监控？.md</title>
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

                    <a class="current-tab" href="20&#32;&#32;服务监控：如何使用&#32;Actuator&#32;组件实现系统监控？.md">20  服务监控：如何使用 Actuator 组件实现系统监控？.md</a>
                    

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
                        <div><h1>20  服务监控：如何使用 Actuator 组件实现系统监控？</h1>
<p>这一讲我们将介绍 Spring Boot 中一个非常有特色的主题——系统监控。</p>
<p>系统监控是 Spring Boot 中引入的一项全新功能，它对应用程序运行状态的管理非常有效。而 Spring Boot Actuator 组件主要通过一系列 HTTP 端点提供的系统监控功能来实现系统监控。因此，接下来我们将引入 Spring Boot Actuator 组件，介绍如何使用它进行系统监控，以及如何对 Actuator 端点进行扩展。</p>
<h3>引入 Spring Boot Actuator 组件</h3>
<p>在初始化 Spring Boot 系统监控功能之前，首先我们需要引入 Spring Boot Actuator 组件，具体操作为在 pom 中添加如下所示的 Maven 依赖：</p>
<pre><code>&lt;dependency&gt;

        &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;

        &lt;artifactId&gt;spring-boot-starter-actuator&lt;/artifactId&gt;

&lt;/dependency&gt;
</code></pre>
<p>请注意，引入 Spring Boot Actuator 组件后，并不是所有的端点都对外暴露。例如，启动 customer-service 时，我们就可以在启动日志中发现如下所示内容：</p>
<pre><code>Exposing 2 endpoint(s) beneath base path '/actuator'
</code></pre>
<p>访问 <a href="http://localhost:8080/actuator">http://localhost:8080/actuator</a> 端点后，我们也会得到如下所示结果。</p>
<pre><code>{

     &quot;_links&quot;:{

         &quot;self&quot;:{

             &quot;href&quot;:&quot;http://localhost:8080/actuator&quot;,

             &quot;templated&quot;:false

         },

         &quot;health-path&quot;:{

             &quot;href&quot;:&quot;http://localhost:8080/actuator/health/{*path}&quot;,

             &quot;templated&quot;:true

         },

         &quot;health&quot;:{

             &quot;href&quot;:&quot;http://localhost:8080/actuator/health&quot;,

             &quot;templated&quot;:false

         },

         &quot;info&quot;:{

             &quot;href&quot;:&quot;http://localhost:8080/actuator/info&quot;,

             &quot;templated&quot;:false

         }

     }

 }
</code></pre>
<p>这种结果就是 HATEOAS 风格的 HTTP 响应。如果我们想看到默认情况下看不到的所有端点，则需要在配置文件中添加如下所示的配置信息。</p>
<pre><code>management:

  endpoints:

    web:

      exposure:

        include: &quot;*&quot;  
</code></pre>
<p>重启应用后，我们就能获取到 Spring Boot Actuator 暴露的所有端点，如下代码所示：</p>
<pre><code>{

     &quot;_links&quot;:{

         &quot;self&quot;:{

             &quot;href&quot;:&quot;http://localhost:8080/actuator&quot;,

             &quot;templated&quot;:false

         },

         &quot;beans&quot;:{

             &quot;href&quot;:&quot;http://localhost:8080/actuator/beans&quot;,

             &quot;templated&quot;:false

         },

         &quot;health&quot;:{

             &quot;href&quot;:&quot;http://localhost:8080/actuator/health&quot;,

             &quot;templated&quot;:false

         },

         &quot;health-path&quot;:{

             &quot;href&quot;:&quot;http://localhost:8080/actuator/health/{*path}&quot;,

             &quot;templated&quot;:true

         },

         &quot;info&quot;:{

             &quot;href&quot;:&quot;http://localhost:8080/actuator/info&quot;,

             &quot;templated&quot;:false

         },

         &quot;conditions&quot;:{

             &quot;href&quot;:&quot;http://localhost:8080/actuator/conditions&quot;,

             &quot;templated&quot;:false

         },

         &quot;configprops&quot;:{

             &quot;href&quot;:&quot;http://localhost:8080/actuator/configprops&quot;,

             &quot;templated&quot;:false

         },

         &quot;env&quot;:{

             &quot;href&quot;:&quot;http://localhost:8080/actuator/env&quot;,

             &quot;templated&quot;:false

         },

         &quot;env-toMatch&quot;:{

             &quot;href&quot;:&quot;http://localhost:8080/actuator/env/{toMatch}&quot;,

             &quot;templated&quot;:true

         },

         &quot;loggers&quot;:{

             &quot;href&quot;:&quot;http://localhost:8080/actuator/loggers&quot;,

             &quot;templated&quot;:false

         },

         &quot;loggers-name&quot;:{

             &quot;href&quot;:&quot;http://localhost:8080/actuator/loggers/{name}&quot;,

             &quot;templated&quot;:true

         },

         &quot;heapdump&quot;:{

             &quot;href&quot;:&quot;http://localhost:8080/actuator/heapdump&quot;,

             &quot;templated&quot;:false

         },

         &quot;threaddump&quot;:{

             &quot;href&quot;:&quot;http://localhost:8080/actuator/threaddump&quot;,

             &quot;templated&quot;:false

         },

         &quot;metrics-requiredMetricName&quot;:{

             &quot;href&quot;:&quot;http://localhost:8080/actuator/metrics/{requiredMetricName}&quot;,

             &quot;templated&quot;:true

         },

         &quot;metrics&quot;:{

             &quot;href&quot;:&quot;http://localhost:8080/actuator/metrics&quot;,

             &quot;templated&quot;:false

         },

         &quot;scheduledtasks&quot;:{

             &quot;href&quot;:&quot;http://localhost:8080/actuator/scheduledtasks&quot;,

             &quot;templated&quot;:false

         },

         &quot;mappings&quot;:{

             &quot;href&quot;:&quot;http://localhost:8080/actuator/mappings&quot;,

             &quot;templated&quot;:false

         }

     }

 }
</code></pre>
<p>根据端点所起到的作用，我们把 Spring Boot Actuator 提供的原生端点分为如下三类。</p>
<ul>
<li><strong>应用配置类：</strong> 主要用来获取应用程序中加载的应用配置、环境变量、自动化配置报告等配置类信息，它们与 Spring Boot 应用密切相关。</li>
<li><strong>度量指标类：</strong> 主要用来获取应用程序运行过程中用于监控的度量指标，比如内存信息、线程池信息、HTTP 请求统计等。</li>
<li><strong>操作控制类：</strong> 在原生端点中只提供了一个关闭应用的端点，即 /shutdown 端点。</li>
</ul>
<p>根据 Spring Boot Actuator 默认提供的端点列表，我们将部分常见端点的类型、路径和描述梳理在如下表格中，仅供参考。</p>
<p><img src="assets/Cip5yGAKfl6Af_yWAAIDoRxLU2E765.png" alt="Drawing 0.png" /></p>
<p>通过访问上表中的各个端点，我们就可以获取自己感兴趣的监控信息了。例如访问了<a href="http://localhost:8082/actuator/health">http://localhost:8082/actuator/health</a>端点，我们就可以得到如下所示的 account-service 基本状态。</p>
<pre><code>{

     &quot;status&quot;:&quot;UP&quot;

 }
</code></pre>
<p>此时，我们看到这个健康状态信息非常简单。</p>
<p>那有没有什么办法可以获取更详细的状态信息呢？答案是：有，而且办法很简单，我们只需要在配置文件中添加如下所示的配置项即可。</p>
<pre><code>management: 

  endpoint:

    health:

      show-details: always
</code></pre>
<p>上述配置项指定了针对 health 端点需要显示它的详细信息。这时，如果我们重启 Spring Boot 应用程序，并重新访问 <a href="http://localhost:8082/actuator/health">http://localhost:8082/actuator/health</a> 端点，就可以获取如下所示的详细信息。</p>
<pre><code>{

     &quot;status&quot;:&quot;UP&quot;,

     &quot;components&quot;:{

         &quot;diskSpace&quot;:{

             &quot;status&quot;:&quot;UP&quot;,

             &quot;details&quot;:{

                 &quot;total&quot;:201649549312,

                 &quot;free&quot;:3434250240,

                 &quot;threshold&quot;:10485760

             }

         },

         &quot;ping&quot;:{

             &quot;status&quot;:&quot;UP&quot;

         }

     }

 }
</code></pre>
<p>如果 Spring Boot Actuator 默认提供的端点信息不能满足业务需求，我们可以对其进行修改和扩展。此时，常见实现方案有两种，一种是扩展现有的监控端点，另一种是自定义新的监控端点。这两种方案我们都会逐一介绍，不过这一讲先来关注如何在现有的监控端点上添加定制化功能。</p>
<h3>扩展 Actuator 端点</h3>
<p>前面我们介绍了 Spring Boot 默认暴露了日常开发中最常见的两个端点：Info 端点和 Health 端点。接下来，我们讨论下如何对这两个端点进行扩展。</p>
<h4>扩展 Info 端点</h4>
<p>Info 端点用于暴露 Spring Boot 应用的自身信息。在 Spring Boot 内部，它把这部分工作委托给了一系列 <a href="https://github.com/spring-projects/spring-boot/tree/v1.4.1.RELEASE/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/info/InfoContributor.java">InfoContributor</a> 对象，而 Info 端点会暴露所有 <a href="https://github.com/spring-projects/spring-boot/tree/v1.4.1.RELEASE/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/info/InfoContributor.java">InfoContributor</a> 对象所收集的各种信息。</p>
<p>在Spring Boot 中包含了很多自动配置的 InfoContributor 对象，常见的 InfoContributor 及其描述如下表所示：</p>
<p><img src="assets/CgqCHmAKfoOARrjaAADoOGMdQb4610.png" alt="Drawing 1.png" /></p>
<p>以上表中的 EnvironmentInfoContributor 为例，通过在配置文件中添加格式以“info”作为前缀的配置段，我们就可以定义 Info 端点暴露的数据。添加完成后，我们将看到所有在“info”配置段下的属性都将被自动暴露。</p>
<p>比如你可以将如下所示配置信息添加到配置文件 application.yml 中：</p>
<pre><code>info:

	app:

	    encoding: UTF-8

	    java:

	        source: 1.8.0_31

	        target: 1.8.0_31
</code></pre>
<p>现在访问 Info 端点，我们就能得到如下的 Environment 信息。</p>
<pre><code>{

     &quot;app&quot;:{

         &quot;encoding&quot;:&quot;UTF-8&quot;,

         &quot;java&quot;:{

             &quot;source&quot;:&quot;1.8.0_31&quot;,

             &quot;target&quot;:&quot;1.8.0_31&quot;

         }

     }

 }
</code></pre>
<p>同时，我们还可以在服务构建时扩展 Info 属性，而不是硬编码这些值。假设使用 Maven，我们就可以按照如下所示的配置重写前面的示例并得到同样的效果。</p>
<pre><code>info: 

	app:

	    encoding: @<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="1060627f7a7573643e7265797c743e637f65627375557e737f74797e7750">[email&#160;protected]</a>

	    java:

	      source: @<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="dfb5bea9bef1a9baadacb6b0b19f">[email&#160;protected]</a>

	      target: @<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="88e2e9fee9a6feedfafbe1e7e6c8">[email&#160;protected]</a>
</code></pre>
<p>很多时候，Spring Boot 自身提供的 Info 端点并不能满足我们的业务需求，这就需要我们编写一个自定义的 InfoContributor 对象。</p>
<p>方法也很简单，我们直接实现 InfoContributor 接口的 contribute() 方法即可。例如，我们希望在 Info 端点中暴露该应用的构建时间，就可以采用如下所示的代码进行操作。</p>
<pre><code>@Component

public class CustomBuildInfoContributor implements InfoContributor {

 

  @Override

  public void contribute(Builder builder) {

      builder.withDetail(&quot;build&quot;, 

          Collections.singletonMap(&quot;timestamp&quot;, new Date())); 

  }

}
</code></pre>
<p>重新构建应用并访问 Info 端口后，我们就能获取如下所示信息。</p>
<pre><code>{

     &quot;app&quot;:{

         &quot;encoding&quot;:&quot;UTF-8&quot;,

         &quot;java&quot;:{

             &quot;source&quot;:&quot;1.8.0_31&quot;,

             &quot;target&quot;:&quot;1.8.0_31&quot;

         }

     },

     &quot;build&quot;:{

         &quot;timestamp&quot;:1604307503710

     }

 }
</code></pre>
<p>这里我们可以看到，CustomBuildInfoContributor 为 Info 端口新增了时间属性。</p>
<h4>扩展 Health 端点</h4>
<p>Health 端点用于检查正在运行的应用程序健康状态，而健康状态信息由 HealthIndicator 对象从 Spring 的 ApplicationContext 中获取。</p>
<p>和 Info 端点一样，Spring Boot 内部也提供了一系列 HealthIndicator 对象供我们实现定制化。在默认情况下，HealthAggregator 会根据 HealthIndicator 的有序列表对每个状态进行排序，从而得到最终的系统状态。</p>
<p>常见的 HealthIndicator 如下表所示：</p>
<table>
<thead>
<tr>
<th><strong>HealthIndicator 名称</strong></th>
<th><strong>描述</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/spring-projects/spring-boot/tree/v2.0.1.RELEASE/spring-boot-project/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/system/DiskSpaceHealthIndicator.java">DiskSpaceHealthIndicator</a></td>
<td>检查磁盘空间是否足够</td>
</tr>
<tr>
<td><a href="https://github.com/spring-projects/spring-boot/tree/v2.0.1.RELEASE/spring-boot-project/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/jdbc/DataSourceHealthIndicator.java">DataSourceHealthIndicator</a></td>
<td>检查是否可以获得连接 DataSource</td>
</tr>
<tr>
<td><a href="https://github.com/spring-projects/spring-boot/tree/v2.0.1.RELEASE/spring-boot-project/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/elasticsearch/ElasticsearchHealthIndicator.java">ElasticsearchHealthIndicator</a></td>
<td>检查 Elasticsearch 集群是否启动</td>
</tr>
<tr>
<td><a href="https://github.com/spring-projects/spring-boot/tree/v2.0.1.RELEASE/spring-boot-project/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/jms/JmsHealthIndicator.java">JmsHealthIndicator</a></td>
<td>检查 JMS 代理是否启动</td>
</tr>
<tr>
<td><a href="https://github.com/spring-projects/spring-boot/tree/v2.0.1.RELEASE/spring-boot-project/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/mail/MailHealthIndicator.java">MailHealthIndicator</a></td>
<td>检查邮件服务器是否启动</td>
</tr>
<tr>
<td><a href="https://github.com/spring-projects/spring-boot/tree/v2.0.1.RELEASE/spring-boot-project/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/mongo/MongoHealthIndicator.java">MongoHealthIndicator</a></td>
<td>检查 Mongo 数据库是否启动</td>
</tr>
<tr>
<td><a href="https://github.com/spring-projects/spring-boot/tree/v2.0.1.RELEASE/spring-boot-project/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/amqp/RabbitHealthIndicator.java">RabbitHealthIndicator</a></td>
<td>检查 RabbitMQ 服务器是否启动</td>
</tr>
<tr>
<td><a href="https://github.com/spring-projects/spring-boot/tree/v2.0.1.RELEASE/spring-boot-project/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/redis/RedisHealthIndicator.java">RedisHealthIndicator</a></td>
<td>检查 Redis 服务器是否启动</td>
</tr>
<tr>
<td><a href="https://github.com/spring-projects/spring-boot/tree/v2.0.1.RELEASE/spring-boot-project/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/solr/SolrHealthIndicator.java">SolrHealthIndicator</a></td>
<td>检查 Solr 服务器是否已启动</td>
</tr>
</tbody>
</table>
<p>Health 端点信息的丰富程度取决于当下应用程序所处的环境，而一个真实的 Health 端点信息如下代码所示：</p>
<pre><code>{

     &quot;status&quot;:&quot;UP&quot;,

     &quot;components&quot;:{

         &quot;db&quot;:{

             &quot;status&quot;:&quot;UP&quot;,

             &quot;details&quot;:{

                 &quot;database&quot;:&quot;MySQL&quot;,

                 &quot;result&quot;:1,

                 &quot;validationQuery&quot;:&quot;/* ping */ SELECT 1&quot;

             }

         },

         &quot;diskSpace&quot;:{

             &quot;status&quot;:&quot;UP&quot;,

             &quot;details&quot;:{

                 &quot;total&quot;:201649549312,

                 &quot;free&quot;:3491287040,

                 &quot;threshold&quot;:10485760

             }

         },

         &quot;ping&quot;:{

             &quot;status&quot;:&quot;UP&quot;

         }

	}

}
</code></pre>
<p>通过以上这些信息，我们就可以判断该环境中是否包含了 MySQL 数据库。</p>
<p>现在，我们还想在 Health 端点中暴露 customer-service 当前运行时状态。</p>
<p>为了进一步明确该服务的状态，我们可以自定义一个 CustomerServiceHealthIndicator 端点专门展示 customer-service 的状态信息，CustomerServiceHealthIndicator 的定义如下所示：</p>
<pre><code>@Component

public class CustomerServiceHealthIndicator implements 

	HealthIndicator {

 

    @Override

    public Health health() {

        try {

	URL url = new 

	URL(&quot;http://localhost:8083/health/&quot;);

	HttpURLConnection conn = (HttpURLConnection) 

	url.openConnection();

            int statusCode = conn.getResponseCode();

            if (statusCode &gt;= 200 &amp;&amp; statusCode &lt; 300) {

                return Health.up().build();

            } else {

                return Health.down().withDetail(&quot;HTTP Status Code&quot;, statusCode).build();

            }

        } catch (IOException e) {

            return Health.down(e).build();

        }

    }

}
</code></pre>
<p>我们需要提供 health() 方法的具体实现并返回一个 Health 结果。该 Health 结果应该包括一个状态，并且可以根据需要添加任何细节信息。</p>
<p>以上代码中，我们使用了一种简单且直接的方式判断配置中心服务“customerservice”是否正在运行。然后我们构建一个 HTTP 请求，并根据 HTTP 响应得出了健康诊断的结论。</p>
<p>如果 HTTP 响应的状态码处于 200~300 之间，我们认为该服务正在运行，此时，Health.up().build() 方法就会返回一种 Up 响应，如下代码所示：</p>
<pre><code>{

    &quot;status&quot;: &quot;UP&quot;,

    &quot;details&quot;: {

        &quot;customerservice&quot;:{

            &quot;status&quot;: &quot;UP&quot;

        }

        …

    }

}
</code></pre>
<p>如果状态码不处于这个区间（例如返回 404，代表服务不可用），Health.down().withDetail().build() 方法就会返回一个 Down 响应，并给出具体的状态码，如下代码所示：</p>
<pre><code>{

    &quot;status&quot;: &quot;DOWN&quot;,

    &quot;details&quot;: {

        &quot;customerservice&quot;:{

            &quot;status&quot;: &quot;DOWN&quot;,

            &quot;details&quot;: {

                &quot;HTTP Status Code&quot;: &quot;404&quot;

            }

        },

        …

    }

}
</code></pre>
<p>如果 HTTP 请求直接抛出了异常，Health.down().build() 方法同样会返回一个 Down 响应，并返回异常信息，效果如下代码所示：</p>
<pre><code>{

    &quot;status&quot;: &quot;DOWN&quot;,

    &quot;details&quot;: {

        &quot;customerservice&quot;:{

            &quot;status&quot;: &quot;DOWN&quot;,

            &quot;details&quot;: {

                &quot;error&quot;: &quot;java.net.ConnectException: Connection refused: connect&quot;

            }

        },

        …

    }

}
</code></pre>
<p>显然，通过扩展 Health 端点为我们实时监控系统中各个服务的正常运行状态提供了很好的支持，我们也可以根据需要构建一系列有用的 HealthIndicator 实现类，并添加报警等监控手段。</p>
<h3>小结与预告</h3>
<p>Spring Boot 内置的 Actuator 组件使得开发人员在管理应用程序运行的状态有了更加直接且高效的手段。</p>
<p>这一讲，我们引入了 Actuator 组件并介绍了该组件提供的一系列核心端点，同时重点分析了 Info 和 Health 这两个基础端点，并给出了对它们进行扩展的系统方法。</p>
<p>系统监控的一大目标是收集和分析系统运行时的度量指标，并基于这些指标判断当前的运行时状态，因此，21 讲我们将讨论如何在系统中嵌入自定义度量指标的实现技巧。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="19&#32;&#32;服务授权：如何基于&#32;Spring&#32;Security&#32;确保请求安全访问？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="21&#32;&#32;指标定制：如何实现自定义度量指标和&#32;Actuator&#32;端点？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434d565ea370ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
