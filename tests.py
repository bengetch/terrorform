from terrorform import terrorform
import pytest


@pytest.fixture(
    scope="module",
    params=[
        {
            "workflow": terrorform.init,
            "kw_args": {},
            "boolean_flags": [],
            "vars_dict": {},
            "expected": "terraform init"
        },
        {
            "workflow": terrorform.init,
            "kw_args": None,
            "boolean_flags": None,
            "vars_dict": None,
            "expected": "terraform init"
        },
        {
            "workflow": terrorform.init,
            "kw_args": {"-chdir": "/tmp/terraform/"},
            "boolean_flags": ["-no-color"],
            "vars_dict": {"deployment-name": "test-deployment", "important_dict": {"var": 8}},
            "expected": "terraform -chdir=\"/tmp/terraform/\" init -no-color -var='deployment-name=test-deployment' -var='important_dict={\"var\": 8}'"
        },
        {
            "workflow": terrorform.apply,
            "kw_args": {},
            "boolean_flags": [],
            "vars_dict": {},
            "expected": "terraform apply -lock=false -auto-approve"
        },
        {
            "workflow": terrorform.apply,
            "kw_args": None,
            "boolean_flags": None,
            "vars_dict": None,
            "expected": "terraform apply -lock=false -auto-approve"
        },
        {
            "workflow": terrorform.apply,
            "kw_args": {"-lock": True},
            "boolean_flags": [],
            "vars_dict": {"num_instances": 8},
            "expected": "terraform apply -lock=true -auto-approve -var='num_instances=8'"
        },
        {
            "workflow": terrorform.destroy,
            "kw_args": {},
            "boolean_flags": [],
            "vars_dict": {},
            "expected": "terraform destroy -lock=false -auto-approve"
        },
        {
            "workflow": terrorform.destroy,
            "kw_args": None,
            "boolean_flags": None,
            "vars_dict": None,
            "expected": "terraform destroy -lock=false -auto-approve"
        },
    ]
)
def get_workflow_inputs(request):
    yield request.param


def test_cli_cmd_construction(get_workflow_inputs):
    """
    Construct a CLI command given some parameters and compare it against the expected output.
    """

    cmd_string = get_workflow_inputs["workflow"](
        get_workflow_inputs["kw_args"],
        get_workflow_inputs["boolean_flags"],
        get_workflow_inputs["vars_dict"],
        dry=True
    )

    assert cmd_string == get_workflow_inputs["expected"]

