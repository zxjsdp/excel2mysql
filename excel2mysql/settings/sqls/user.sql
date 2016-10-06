CREATE TABLE IF NOT EXISTS `user_tmp` (
    `id` int(11) unsigned not null auto_increment comment '主键 ID',
    `name` varchar(30) not null default '' comment '名字',
    `age` int(11) unsigned not null default '0' comment '年龄',
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
PRIMARY KEY (`id`),
KEY `ix_created_at` (`created_at`),
KEY `ix_updated_at` (`updated_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='User 临时表';
