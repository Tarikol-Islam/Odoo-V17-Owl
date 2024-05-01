/** @odoo-module **/

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class OwlSaleDashboard extends Component {
    setup() {
    }
}

OwlSaleDashboard.template = 'owl_components.owl_sale_dashboard';
registry.category("actions").add("owl_sale_dashboard", OwlSaleDashboard);
